# Integração com ActivePieces

ActivePieces é uma alternativa open-source ao Zapier/n8n.

## HTTP Request Piece

1. Adicione um passo **HTTP**.
2. Action: **Send HTTP Request**.
3. **Method:** `POST`.
4. **URL:** `https://gateway.apibrasil.io/api/v2/cep/cep`.
5. **Headers:**
   - `Authorization`: `Bearer ...`
   - `DeviceToken`: `...`
6. **Body:**
   ```json
   {
     "cep": "{{ steps.trigger.cep }}"
   }
   ```

Simples e direto, usando a API REST.
