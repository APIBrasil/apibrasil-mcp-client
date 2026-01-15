# Integração com Vercel (Serverless Functions)

Exemplo de uma Serverless Function em Node.js que consome a APIBrasil.

## Código (`api/consulta-cep.js`)

```javascript
export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { cep } = req.body;
  
  // Chamada REST direta (mais leve que carregar SDK MCP em serverless)
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
  res.status(200).json(data);
}
```

## Configuração
Adicione as variáveis de ambiente `APIBRASIL_TOKEN` e `APIBRASIL_DEVICE_TOKEN` no painel da Vercel.
