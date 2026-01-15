# Integração com Typebot

O Typebot executa fluxos rápidos e stateless. O protocolo MCP (que é stateful via SSE) não é ideal para conexão direta via blocos nativos HTTP do Typebot.

## Como Integrar

### Opção 1: Via API REST Direta (Recomendado)
Como este servidor MCP é um wrapper da APIBrasil, a forma mais robusta no Typebot é chamar a API direta:
- Use o bloco **HTTP Request**.
- URL: `https://gateway.apibrasil.io/api/v2/...`
- Auth: Bearer Token.

### Opção 2: Via Cloud Function / Wrapper
Se precisar *obrigatoriamente* passar pelo servidor MCP (ex: para aproveitar a lógica de ferramentas unificada):

1. Crie uma **Cloud Function** (AWS Lambda / Vercel Edge) que faz o handshake MCP.
2. Chame essa função no Typebot via bloco HTTP.

Não é possível conectar SSE nativamente dentro do fluxo de chat padrão do Typebot.
