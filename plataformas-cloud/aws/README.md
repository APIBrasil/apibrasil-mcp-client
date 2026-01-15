# Integração com AWS Lambda

## Código (Node.js 18.x)

```javascript
exports.handler = async (event) => {
  const body = JSON.parse(event.body);
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

  return {
    statusCode: 200,
    body: JSON.stringify(data),
  };
};
```

## AWS Bedrock Agents
Para usar com Bedrock Agents, defina um **Action Group** com o schema OpenAPI da APIBrasil.
