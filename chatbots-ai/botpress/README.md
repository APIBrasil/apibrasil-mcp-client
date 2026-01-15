# Integração com Botpress

## Execute Code Card

No Botpress Studio, adicione um card **Execute Code** no seu fluxo.

```javascript
// Input variables
const cep = workflow.cep; // Supondo que você capturou isso antes
const token = env.APIBRASIL_TOKEN;
const device = env.APIBRASIL_DEVICE;

try {
  const response = await axios.post(
    'https://gateway.apibrasil.io/api/v2/cep/cep',
    { cep: cep },
    {
      headers: {
        'Authorization': `Bearer ${token}`,
        'DeviceToken': device
      }
    }
  );

  // Output
  workflow.endereco = response.data;
  workflow.found = true;
} catch (error) {
  workflow.found = false;
  console.log(error);
}
```

Certifique-se de configurar as variáveis de ambiente no Botpress Cloud.
