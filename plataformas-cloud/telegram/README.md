# Integração com Telegram (Telegraf)

## Código (`bot.js`)

```javascript
const { Telegraf } = require('telegraf');
const bot = new Telegraf(process.env.TELEGRAM_TOKEN);

bot.command('cep', async (ctx) => {
  const cep = ctx.message.text.split(' ')[1];
  if (!cep) return ctx.reply('Por favor, envie o CEP. Ex: /cep 01001000');
  
  try {
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
    ctx.reply(`📦 Endereço encontrado:\n${data.logradouro}\n${data.bairro}\n${data.localidade} - ${data.uf}`);
  } catch (e) {
    ctx.reply('Erro ao consultar CEP.');
  }
});

bot.launch();
```
