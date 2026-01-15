# Integração com Google Sheets (Apps Script)

Automatize planilhas com scripts customizados.

## Código (Apps Script)

1. No Google Sheets, vá em **Extensões** > **Apps Script**.
2. Cole o código abaixo:

```javascript
const API_BASE = "https://gateway.apibrasil.io/api/v2";
const BEARER = "SEU_BEARER";
const DEVICE_TOKEN = "SEU_DEVICE_TOKEN";

/**
 * Consulta CEP na APIBrasil
 * @param {string} cep O CEP a consultar
 * @return O endereço formatado ou JSON
 * @customfunction
 */
function APIBRASIL_CEP(cep) {
  if (!cep) return "Informe o CEP";
  
  const url = `${API_BASE}/cep/cep`;
  const payload = {
    cep: cep.toString()
  };
  
  const options = {
    method: 'post',
    contentType: 'application/json',
    headers: {
      'Authorization': `Bearer ${BEARER}`,
      'DeviceToken': DEVICE_TOKEN
    },
    payload: JSON.stringify(payload),
    muteHttpExceptions: true
  };
  
  try {
    const response = UrlFetchApp.fetch(url, options);
    const json = JSON.parse(response.getContentText());
    
    // Retorna o logradouro ou todo o JSON se preferir
    return json.logradouro ? `${json.logradouro}, ${json.bairro} - ${json.localidade}/${json.uf}` : JSON.stringify(json);
  } catch (e) {
    return "Erro: " + e.message;
  }
}
```

3. Salve e use na célula: `=APIBRASIL_CEP("01001-000")`
