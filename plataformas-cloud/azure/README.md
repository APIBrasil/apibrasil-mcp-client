# Integração com Azure Functions

## Código (JavaScript v4)

```javascript
const { app } = require('@azure/functions');

app.http('consultaCep', {
    methods: ['POST'],
    authLevel: 'anonymous',
    handler: async (request, context) => {
        const body = await request.json();
        const { cep } = body;

        const response = await fetch('https://gateway.apibrasil.io/api/v2/cep/cep', {
            method: 'POST',
            headers: {
              'Authorization': `Bearer ${process.env.APIBRASIL_TOKEN}`,
              'DeviceToken': process.env.APIBRASIL_DEVICE_TOKEN,
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({ cep })
        });

        const data = await response.json();
        return { body: JSON.stringify(data) };
    }
});
```

## Azure OpenAI
Use a funcionalidade "Add your data" ou Function Calling conectando a este endpoint.
