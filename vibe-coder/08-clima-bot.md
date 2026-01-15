# Bot de Previsão do Tempo (Cron)

Serviço "Wake-up Call" que envia a previsão do tempo para uma lista de VIPs todas as manhãs.

## Onde usar
Salve como `daily_weather.js`.

## Setup
`npm install node-cron axios dotenv`

## Código Otimizado

```javascript
require('dotenv').config();
const cron = require('node-cron');
const axios = require('axios');

const CONFIG = {
    city: process.env.WEATHER_CITY || 'São Paulo',
    subscribers: (process.env.WEATHER_SUBSCRIBERS || '').split(','), // Lista separada por vírgula
    token: process.env.APIBRASIL_TOKEN,
    device: process.env.APIBRASIL_DEVICE_TOKEN,
    schedule: '0 7 * * *' // 07:00 AM
};

async function getWeather() {
    try {
        const { data } = await axios.post(
            'https://gateway.apibrasil.io/api/v2/weather/city',
            { city: CONFIG.city },
            { headers: { Authorization: `Bearer ${CONFIG.token}`, DeviceToken: CONFIG.device } }
        );
        return data;
    } catch (error) {
        console.error('Erro ao obter clima:', error.message);
        return null;
    }
}

async function broadcast() {
    console.log('🌦️ Iniciando broadcast matinal...');
    
    const weather = await getWeather();
    if (!weather) return;

    // Template da Mensagem
    const msg = `☀️ *Bom dia!* Previsão para hoje em ${CONFIG.city}:\n\n` +
                `🌡️ Temp: ${weather.temp}°C\n` +
                `💧 Umidade: ${weather.humidity}%\n` +
                `👁️ Condição: ${weather.description}`;

    for (const phone of CONFIG.subscribers) {
        if (!phone) continue;
        try {
            await axios.post(
                'https://gateway.apibrasil.io/api/v2/whatsapp/sendText',
                { number: phone.trim(), text: msg },
                { headers: { Authorization: `Bearer ${CONFIG.token}`, DeviceToken: CONFIG.device } }
            );
            console.log(`✅ Enviado para ${phone}`);
        } catch (error) {
            console.error(`❌ Falha para ${phone}:`, error.message);
        }
        
        // Pequeno delay para não sobrecarregar
        await new Promise(r => setTimeout(r, 2000));
    }
}

// Inicia o agendamento
console.log(`⏰ Agendado para: ${CONFIG.schedule}`);
cron.schedule(CONFIG.schedule, broadcast);

// Modo Debug (Descomente para testar agora)
// broadcast();
```
