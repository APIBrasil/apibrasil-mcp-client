# Integração com Google Cloud (Cloud Functions)

## Código (`index.js`)

```javascript
const functions = require('@google-cloud/functions-framework');

functions.http('consultaCep', async (req, res) => {
  if (req.method !== 'POST') {
    return res.status(405).send('Method Not Allowed');
  }

  const { cep } = req.body;

  try {
    const apiResponse = await fetch('https://gateway.apibrasil.io/api/v2/cep/cep', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${process.env.APIBRASIL_TOKEN}`,
          'DeviceToken': process.env.APIBRASIL_DEVICE_TOKEN,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ cep })
    });
    
    const data = await apiResponse.json();
    res.json(data);
  } catch (error) {
    res.status(500).send(error.message);
  }
});
```

## Vertex AI Agent Builder
Se estiver usando o Vertex AI, adicione a APIBrasil como uma **OpenAPI Tool** importando o schema JSON (similar ao exemplo do OpenAI GPTs).
