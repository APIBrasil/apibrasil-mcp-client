# Integração com n8n

O n8n pode consumir o servidor MCP de duas formas: usando o nó **HTTP Request** (para chamadas manuais) ou o nó **Code** (para lidar com o handshake Streamable HTTP).

Como o MCP exige um handshake (POST `initialize`) para obter o `Mcp-Session-Id`, a melhor abordagem no n8n é via **Code Node**.

## Exemplo de Code Node (JavaScript)

Adicione um nó "Code" e use este script para fazer o handshake e a chamada:

```javascript
// Configuração
const SERVER_URL = 'https://mcp.apibrasil.cloud/mcp';

// 1. Handshake Streamable HTTP: POST initialize -> o Mcp-Session-Id volta no header
const initResp = await this.helpers.httpRequest({
  method: 'POST',
  url: SERVER_URL,
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json, text/event-stream',
  },
  body: {
    jsonrpc: '2.0',
    id: 'init',
    method: 'initialize',
    params: {
      protocolVersion: '2025-06-18',
      clientInfo: { name: 'n8n', version: '1.0.0' },
      capabilities: {},
    },
  },
  json: true,
  returnFullResponse: true,
});
const sessionId = initResp.headers['mcp-session-id'];

// 2. tools/call usando o Mcp-Session-Id no header
//    body: { jsonrpc: '2.0', id: 1, method: 'tools/call',
//            params: { name: 'cep_lookup',
//                      arguments: { cep: '01001000', bearer: 'SEU_BEARER', deviceToken: 'SEU_DEVICE_TOKEN' } } }

// RECOMENDAÇÃO: para automações transacionais (n8n), a API REST direta
// (https://gateway.apibrasil.io) costuma ser mais simples que gerenciar sessão MCP,
// pois o MCP é desenhado para manter estado com Agentes de IA.
```

### Alternativa: AI Agent Node (LangChain)

Se você estiver usando os nós de **AI Agent** do n8n:

1. Use o nó **"Custom Tool"** (ou MCP Tool se disponível na sua versão).
2. Configure a ferramenta para fazer o POST no endpoint JSON-RPC do MCP, assumindo que você gerencie a sessão externamente.

*Dica: Para automações transacionais (como n8n), use a API REST direta. Use este servidor MCP apenas quando conectar o n8n a um Agente de IA que fala MCP nativamente.*
