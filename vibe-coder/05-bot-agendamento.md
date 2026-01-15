# Bot de Agendamento Inteligente (Webhook)

Um servidor intermediário (Middleware) que recebe mensagens do WhatsApp, processa intenções básicas e responde.

## Onde usar
Copie e cole em um arquivo `server.js` em um projeto Node.js (Express).

## Código Otimizado

```javascript
require('dotenv').config();
const express = require('express');
const axios = require('axios');

const app = express();
app.use(express.json());

const CONFIG = {
    port: process.env.PORT || 3000,
    apiToken: process.env.APIBRASIL_TOKEN,
    deviceToken: process.env.APIBRASIL_DEVICE_TOKEN
};

// Funções Auxiliares
async function sendWhatsApp(to, message) {
    try {
        await axios.post('https://gateway.apibrasil.io/api/v2/whatsapp/sendText', {
            number: to,
            text: message
        }, {
            headers: {
                'Authorization': `Bearer ${CONFIG.apiToken}`,
                'DeviceToken': CONFIG.deviceToken
            }
        });
    } catch (err) {
        console.error(`Falha no envio para ${to}:`, err.message);
    }
}

// Processamento de NLP (Simulado)
function detectIntent(text) {
    const t = text.toLowerCase();
    if (t.includes('agendar') || t.includes('marcar')) return 'SCHEDULE';
    if (t.includes('preço') || t.includes('valor') || t.includes('quanto')) return 'PRICING';
    if (t.includes('endereço') || t.includes('onde')) return 'LOCATION';
    return 'UNKNOWN';
}

// Webhook Handler
app.post('/webhook', async (req, res) => {
    try {
        const event = req.body;
        
        // Validação básica do payload (adapte conforme sua versão da API)
        if (event?.event === 'onMessage' && !event.fromMe) {
            const sender = event.contact?.number || event.from;
            const content = event.body || event.text || '';
            
            console.log(`📩 Mensagem de ${sender}: ${content}`);

            const intent = detectIntent(content);
            let reply = '';

            switch (intent) {
                case 'SCHEDULE':
                    reply = '🗓️ Para agendar, acesse nossa agenda oficial: https://cal.com/sua-empresa';
                    break;
                case 'PRICING':
                    reply = '💰 Nossos planos começam em R$ 99/mês. Gostaria de receber o PDF?';
                    break;
                case 'LOCATION':
                    reply = '📍 Estamos na Av. Paulista, 1000 - São Paulo/SP.';
                    break;
                default:
                    // Opcional: Não responder tudo para não parecer spam
                    // reply = 'Olá! Sou um assistente virtual. Posso ajudar com Agendamento, Preços ou Endereço.';
            }

            if (reply) {
                await sendWhatsApp(sender, reply);
            }
        }
    } catch (err) {
        console.error('Erro no processamento do webhook:', err);
    }

    // Sempre retornar 200 OK rápido para a API não reenviar
    res.sendStatus(200);
});

app.listen(CONFIG.port, () => {
    console.log(`🤖 Bot rodando na porta ${CONFIG.port}`);
});
```
