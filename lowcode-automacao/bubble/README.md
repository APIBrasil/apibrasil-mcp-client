# Integração com Bubble.io

O Bubble conecta-se via **API Connector**.

## Configuração

1. Instale o plugin **API Connector**.
2. Adicione uma nova API: "APIBrasil".
3. Adicione uma chamada (Call):
   - **Method:** POST (ou GET conforme endpoint).
   - **URL:** `https://gateway.apibrasil.io/api/v2/...`
   - **Headers:** `Authorization: Bearer [SeuToken]`

## Uso com MCP (Avançado)
Se você estiver construindo um Chatbot AI no Bubble e quiser usar o MCP:

1. Você precisará de um plugin de **Server-Side Action** (Node.js).
2. Instale o SDK `@modelcontextprotocol/sdk` no plugin.
3. Use o código de cliente Node.js (veja pasta `examples/linguagens/nodejs`) dentro da ação do plugin para conectar e buscar dados.
