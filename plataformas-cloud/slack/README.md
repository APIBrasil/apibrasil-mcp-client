# Integração com Slack (Bolt.js)

Crie um bot Slack que consulta a APIBrasil.

## Código (`app.js`)

```javascript
const { App } = require('@slack/bolt');

const app = new App({
  token: process.env.SLACK_BOT_TOKEN,
  signingSecret: process.env.SLACK_SIGNING_SECRET
});

app.command('/cep', async ({ command, ack, respond }) => {
  await ack();
  
  const cep = command.text;
  
  // Chamada à API
  const res = await fetch('https://gateway.apibrasil.io/api/v2/cep/cep', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${process.env.APIBRASIL_TOKEN}`,
          'DeviceToken': process.env.APIBRASIL_DEVICE_TOKEN,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ cep })
    });
    
  const data = await res.json();
  
  await respond(`Endereço: ${data.logradouro}, ${data.bairro} - ${data.localidade}/${data.uf}`);
});

(async () => {
  await app.start(process.env.PORT || 3000);
  console.log('⚡️ Bolt app is running!');
})();
```
