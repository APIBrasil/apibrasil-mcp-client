# Integração com Flowise

O Flowise é uma ferramenta Low-Code para construir LLM Apps e suporta integração via **Custom Tools**.

## Passo a Passo

1. No canvas do Flowise, procure por **Tools**.
2. Escolha **Custom Tool**.
3. Defina o Schema da ferramenta (copie do código fonte da tool desejada, ex: `cep_lookup`).
4. No campo "Javascript Function", implemente a chamada ao servidor MCP:

```javascript
/* 
  Para Flowise, o ideal é usar o SDK do MCP se o ambiente permitir,
  ou fazer a chamada HTTP POST direta se você já tiver um sessionId fixo (avançado).
*/
const fetch = require('node-fetch');

// ... lógica de chamada ...
```

**Novidade:** O Flowise está implementando suporte nativo ao protocolo MCP. Assim que lançado, você poderá apenas:
1. Arrastar um nó "MCP Client".
2. Colocar a URL: `https://mcp.apibrasil.cloud/mcp`.
3. Conectar ao seu Agente.
