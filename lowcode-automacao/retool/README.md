# Integração com Retool

Retool é ideal para painéis internos.

## Configuração do Resource

1. Vá em **Resources** > **Create New**.
2. Selecione **REST API**.
3. **Name:** APIBrasil
4. **Base URL:** `https://gateway.apibrasil.io/api/v2`
5. **Headers:**
   - `Authorization`: `Bearer YOUR_TOKEN`
   - `DeviceToken`: `YOUR_DEVICE_TOKEN`
6. Clique em **Create Resource**.

## Usando em um App

1. Crie uma nova **Query**.
2. Resource: `APIBrasil`.
3. Action Type: `POST`.
4. Endpoint: `cep/cep` (exemplo).
5. Body: Raw JSON
   ```json
   {
     "cep": "{{ textInput1.value }}"
   }
   ```
6. Use `{{ query1.data }}` nos componentes visuais.
