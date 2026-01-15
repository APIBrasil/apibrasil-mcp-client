# Bot de Rastreio de Encomendas

Script profissional em Node.js para monitorar encomendas e notificar via WhatsApp. Ideal para e-commerce ou uso pessoal.

## Onde usar
Copie e cole em um arquivo `rastreio-service.js`.

## Prompt para Gerar (Se usar IA)
"Crie um serviço em Node.js que monitora uma lista de códigos de rastreio dos Correios usando a APIBrasil. Use `axios` para requisições, `dotenv` para configuração e um arquivo JSON local como banco de dados simples para evitar notificações duplicadas."

## Código Otimizado (Manual)

```javascript
require('dotenv').config();
const axios = require('axios');
const fs = require('fs/promises');
const path = require('path');

// Configuração via Variáveis de Ambiente
const CONFIG = {
    token: process.env.APIBRASIL_TOKEN,
    deviceToken: process.env.APIBRASIL_DEVICE_TOKEN,
    whatsappNumber: process.env.WHATSAPP_ADMIN_NUMBER, // 5511999999999
    checkInterval: 30 * 60 * 1000 // 30 minutos
};

const DB_FILE = path.join(__dirname, 'tracking_db.json');
const TRACKING_CODES = ['AA123456789BR', 'BB987654321BR']; // Pode vir de um banco real

async function loadCache() {
    try {
        const data = await fs.readFile(DB_FILE, 'utf8');
        return JSON.parse(data);
    } catch {
        return {};
    }
}

async function saveCache(data) {
    await fs.writeFile(DB_FILE, JSON.stringify(data, null, 2));
}

async function notifyWhatsApp(message) {
    try {
        await axios.post('https://gateway.apibrasil.io/api/v2/whatsapp/sendText', {
            number: CONFIG.whatsappNumber,
            text: message
        }, {
            headers: {
                'Authorization': `Bearer ${CONFIG.token}`,
                'DeviceToken': CONFIG.deviceToken
            }
        });
        console.log('✅ Notificação enviada');
    } catch (error) {
        console.error('❌ Erro no envio WhatsApp:', error.message);
    }
}

async function checkTracking() {
    console.log(`🔍 Iniciando verificação: ${new Date().toISOString()}`);
    const cache = await loadCache();
    let hasChanges = false;

    for (const code of TRACKING_CODES) {
        try {
            const { data } = await axios.post('https://gateway.apibrasil.io/api/v2/correios/rastreio', { code }, {
                headers: {
                    'Authorization': `Bearer ${CONFIG.token}`,
                    'DeviceToken': CONFIG.deviceToken
                }
            });

            // Lógica de Detecção de Mudança
            const lastEvent = data.events?.[0];
            if (!lastEvent) continue;

            const eventHash = `${lastEvent.date}-${lastEvent.time}-${lastEvent.status}`;
            
            if (cache[code] !== eventHash) {
                const msg = `📦 *Atualização de Rastreio*\n\n🔖 Código: ${code}\n📍 Status: ${lastEvent.status}\n🌎 Local: ${lastEvent.location}\n📅 Data: ${lastEvent.date} às ${lastEvent.time}`;
                
                await notifyWhatsApp(msg);
                cache[code] = eventHash;
                hasChanges = true;
            }
        } catch (error) {
            console.error(`⚠️ Falha ao consultar ${code}:`, error.message);
        }
    }

    if (hasChanges) await saveCache(cache);
}

// Loop Principal
console.log('🚀 Serviço de Rastreio Iniciado');
checkTracking();
setInterval(checkTracking, CONFIG.checkInterval);
```
