# Integração com OpenAI GPTs (Custom Actions)

Para conectar seu GPT personalizado à APIBrasil, você deve configurar uma **Action** usando o esquema OpenAPI (Swagger).

## Passo a Passo

1. Crie um novo GPT em [chat.openai.com/create](https://chat.openai.com/create).
2. Vá em **Configure** > **Create new action**.
3. Em **Authentication**, selecione **API Key** -> **Bearer**.
4. Cole o Schema OpenAPI.

> **Nota:** O servidor MCP usa JSON-RPC, que não é compatível diretamente com GPT Actions. Você deve apontar a Action para a **API REST original** (`gateway.apibrasil.io`).

## Exemplo de Schema (Parcial)

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "APIBrasil Tools",
    "description": "Ferramentas para consulta de CEP, CNPJ, Veículos, etc.",
    "version": "1.0.0"
  },
  "servers": [
    {
      "url": "https://gateway.apibrasil.io/api/v2"
    }
  ],
  "paths": {
    "/cep/cep": {
      "post": {
        "description": "Consulta dados de um CEP",
        "operationId": "consultarCep",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "cep": { "type": "string" }
                }
              }
            }
          }
        },
        "responses": {
          "200": { "description": "Dados do endereço" }
        }
      }
    }
  }
}
```
