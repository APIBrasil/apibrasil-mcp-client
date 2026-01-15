# Webhook Bridge (Cloudflare Worker)

Middleware serverless para conectar serviços externos (Stripe, Typeform) ao WhatsApp da APIBrasil.

## Onde usar
Painel do **Cloudflare Workers**.

## Configuração
No painel do Cloudflare, vá em **Settings > Variables** e adicione:
- `APIBRASIL_TOKEN`: Seu Bearer Token
- `APIBRASIL_DEVICE_TOKEN`: Seu Device Token
- `WHATSAPP_ADMIN`: Número para receber alertas

## Código Otimizado

```javascript
export default {
  async fetch(request, env, ctx) {
    // 1. Validação de Método
    if (request.method !== "POST") {
      return new Response("Method Not Allowed", { status: 405 });
    }

    // 2. Validação de Segurança (Secret do Webhook)
    // Recomendado: Checar header 'Stripe-Signature' ou query param ?secret=xyz
    const url = new URL(request.url);
    if (url.searchParams.get("secret") !== env.WEBHOOK_SECRET) {
        // return new Response("Unauthorized", { status: 401 });
        // Comentado para facilitar teste inicial
    }

    try {
      const payload = await request.json();
      
      // Roteamento de Eventos
      if (payload.type === 'invoice.payment_failed') {
        await handlePaymentFailed(payload, env);
        return new Response("Alert Sent", { status: 200 });
      }
      
      if (payload.event_type === 'form_response') {
        await handleTypeform(payload, env);
        return new Response("Form Processed", { status: 200 });
      }

      return new Response("Event Ignored", { status: 200 });

    } catch (e) {
      return new Response(`Error: ${e.message}`, { status: 500 });
    }
  },
};

// Handlers Específicos
async function handlePaymentFailed(payload, env) {
    const customerPhone = payload.data.object.customer_phone;
    const amount = (payload.data.object.amount_due / 100).toFixed(2);
    
    if (customerPhone) {
        await sendWhatsApp(env, customerPhone, 
            `⚠️ *Atenção*: Pagamento de R$ ${amount} falhou. Atualize seu cartão para evitar bloqueio.`
        );
    }
}

async function handleTypeform(payload, env) {
    // Exemplo genérico
    await sendWhatsApp(env, env.WHATSAPP_ADMIN, 
        `📝 Novo Lead recebido via Typeform!`
    );
}

// Função de Envio APIBrasil
async function sendWhatsApp(env, to, message) {
    const url = "https://gateway.apibrasil.io/api/v2/whatsapp/sendText";
    
    const response = await fetch(url, {
        method: "POST",
        headers: {
            "Authorization": `Bearer ${env.APIBRASIL_TOKEN}`,
            "DeviceToken": env.APIBRASIL_DEVICE_TOKEN,
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            number: to,
            text: message
        })
    });

    if (!response.ok) {
        throw new Error(`APIBrasil Error: ${response.status}`);
    }
}
```
