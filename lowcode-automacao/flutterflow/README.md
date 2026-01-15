# Integração com FlutterFlow

## API Calls

1. No menu esquerdo, vá em **API Calls**.
2. Clique em **+ Add API Call**.
3. **Name:** `ConsultarCEP`.
4. **Method:** `POST`.
5. **API URL:** `https://gateway.apibrasil.io/api/v2/cep/cep`.
6. **Headers:**
   ```
   Authorization: Bearer [Token]
   DeviceToken: [DeviceToken]
   Content-Type: application/json
   ```
7. **Body:** JSON
   ```json
   {
     "cep": "01001000"
   }
   ```
   (Crie uma variável para o CEP e substitua no body).
8. Clique em **Test API Call** e depois em **Add Call**.

Agora você pode usar essa ação nos botões e eventos do seu app Flutter.
