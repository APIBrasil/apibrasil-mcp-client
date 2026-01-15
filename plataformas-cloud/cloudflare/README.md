# Integração com Cloudflare Workers

## Código (`worker.js`)

```javascript
export default {
  async fetch(request, env, ctx) {
    if (request.method !== "POST") {
        return new Response("Method not allowed", { status: 405 });
    }
    
    const { cep } = await request.json();

    const response = await fetch('https://gateway.apibrasil.io/api/v2/cep/cep', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${env.APIBRASIL_TOKEN}`,
        'DeviceToken': env.APIBRASIL_DEVICE_TOKEN,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ cep })
    });

    const data = await response.json();
    return Response.json(data);
  },
};
```
