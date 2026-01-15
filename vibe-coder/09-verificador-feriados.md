# Verificador de Dias Úteis (Smart Calendar)

Módulo utilitário para verificar se uma data é dia útil, considerando fins de semana e feriados nacionais (via API). Inclui sistema de Cache em memória para performance.

## Onde usar
Copie e cole como `utils/calendar.js` em seu projeto backend.

## Código Otimizado

```javascript
const axios = require('axios');

// Cache simples em memória (Ano -> Lista de Feriados)
const holidayCache = new Map();

/**
 * Verifica se uma data é dia útil (Business Day)
 * @param {Date} dateObj Data a verificar
 * @param {string} token APIBrasil Bearer Token
 * @returns {Promise<boolean>} True se for dia útil
 */
async function isBusinessDay(dateObj = new Date(), token) {
    // 1. Validação de Fim de Semana (Sábado/Domingo)
    const dayOfWeek = dateObj.getDay();
    if (dayOfWeek === 0 || dayOfWeek === 6) {
        return false;
    }

    const year = dateObj.getFullYear();
    const dateString = dateObj.toISOString().split('T')[0]; // YYYY-MM-DD

    try {
        // 2. Busca feriados (com Cache)
        let holidays = holidayCache.get(year);

        if (!holidays) {
            if (!token) throw new Error("Token obrigatório para consulta de feriados");
            
            const { data } = await axios.post(
                'https://gateway.apibrasil.io/api/v2/holidays/feriados',
                { year: year.toString(), type: 'nacional' },
                { 
                    headers: { Authorization: `Bearer ${token}` } 
                }
            );
            
            holidays = data.map(h => h.date); // Assumindo formato YYYY-MM-DD
            holidayCache.set(year, holidays);
            console.log(`📅 Feriados de ${year} cacheados.`);
        }

        // 3. Verifica colisão
        return !holidays.includes(dateString);

    } catch (error) {
        console.warn(`⚠️ Falha ao verificar feriados: ${error.message}. Assumindo dia útil.`);
        // Fail-open: Se API falhar, assume que é dia útil para não travar processos
        return true; 
    }
}

module.exports = { isBusinessDay };
```
