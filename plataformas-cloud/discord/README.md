# Integração com Discord (Discord.js)

## Código (`bot.js`)

```javascript
const { Client, GatewayIntentBits } = require('discord.js');
const client = new Client({ intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMessages, GatewayIntentBits.MessageContent] });

client.on('messageCreate', async message => {
  if (message.content.startsWith('!cep')) {
    const cep = message.content.split(' ')[1];
    
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
    message.reply(`📍 ${data.logradouro}, ${data.bairro} - ${data.localidade}/${data.uf}`);
  }
});

client.login(process.env.DISCORD_TOKEN);
```
