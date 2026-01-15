# Integração com Microsoft Power Automate

## Criando um Custom Connector

1. Vá em **Data** > **Custom Connectors**.
2. **New custom connector** > **Create from blank**.
3. **General:**
   - Host: `gateway.apibrasil.io`
   - Base URL: `/api/v2`
   - Scheme: `HTTPS`
4. **Security:**
   - Type: `API Key`
   - Parameter label: `Authorization`
   - Parameter name: `Authorization`
   - Location: `Header`
5. **Definition:**
   - Crie uma Action (ex: `ConsultarCEP`).
   - Importe do exemplo (Request):
     - Verb: `POST`
     - URL: `https://gateway.apibrasil.io/api/v2/cep/cep`
     - Body: `{"cep": "01001000"}`
6. Salve e teste.

Agora você pode usar o bloco "APIBrasil" em qualquer fluxo do Power Automate.
