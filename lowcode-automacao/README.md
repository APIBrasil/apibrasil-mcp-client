# Integração com n8n

O n8n pode consumir o servidor MCP de duas formas: usando o nó **HTTP Request** (para chamadas manuais) ou o nó **Code** (para lidar com o handshake SSE).

Como o MCP exige uma conexão SSE para obter o `sessionId`, a melhor abordagem no n8n é via **Code Node**.

## Exemplo de Code Node (JavaScript)

Adicione um nó "Code" e use este script para fazer uma chamada rápida (Handshake + Execução):

```javascript
// Configuração
const SERVER_URL = 'https://mcp.apibrasil.cloud/mcp';
const TOOL_NAME = 'cep_lookup';
const TOOL_ARGS = {
  cep: '01001000',
  bearer: 'SEU_BEARER',
  deviceToken: 'SEU_DEVICE_TOKEN'
};

// 1. Obtém Session ID via GET (simulado)
// Nota: Em produção, o MCP requer manter a conexão SSE aberta. 
// Para chamadas únicas (stateless), recomenda-se usar a API direta da APIBrasil.
// Mas para testar via MCP, você pode tentar capturar o primeiro evento:

const response = await this.helpers.request({
  method: 'GET',
  url: SERVER_URL,
  returnFullResponse: true,
  headers: {
    'Accept': 'text/event-stream'
  }
});

// Parseia o SessionID do stream (simplificado)
// O n8n pode não suportar streams infinitos no HTTP Request padrão.
// RECOMENDAÇÃO: Para n8n, use a API oficial REST da APIBrasil diretamente 
// (https://gateway.apibrasil.io) em vez de passar pelo protocolo MCP,
// pois o MCP é desenhado para manter estado com Agentes de IA.
```

### Alternativa: AI Agent Node (LangChain)

Se você estiver usando os nós de **AI Agent** do n8n:

1. Use o nó **"Custom Tool"** (ou MCP Tool se disponível na sua versão).
2. Configure a ferramenta para fazer o POST no endpoint JSON-RPC do MCP, assumindo que você gerencie a sessão externamente.

*Dica: Para automações transacionais (como n8n), use a API REST direta. Use este servidor MCP apenas quando conectar o n8n a um Agente de IA que fala MCP nativamente.*
