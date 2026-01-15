# Integração com Voiceflow

## API Step

1. Arraste um bloco **API** para o canvas.
2. **Method:** `POST`
3. **URL:** `https://gateway.apibrasil.io/api/v2/cep/cep`
4. **Headers:**
   - `Authorization`: `Bearer {seu_token}` (ou variável `{token}`)
   - `DeviceToken`: `{seu_device_token}`
5. **Body (JSON):**
   ```json
   {
     "cep": "{cep_usuario}"
   }
   ```
6. **Capture Response:**
   - Mapeie `response.logradouro` para a variável `{logradouro}`.

O Voiceflow lida nativamente com a chamada REST.
