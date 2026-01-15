# Consumindo APIBrasil MCP com Node.js

Este exemplo usa o SDK oficial do MCP para TypeScript/Node.js.

## 1. Instalação

Abra seu terminal na pasta do projeto e instale as dependências:

```bash
npm install @modelcontextprotocol/sdk eventsource
```

## 2. Código (index.js ou index.ts)

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { SSEClientTransport } from "@modelcontextprotocol/sdk/client/sse.js";
import { EventSource } from "eventsource";

// Polyfill para Node.js (necessário pois SSE usa EventSource do browser)
global.EventSource = EventSource;

async function main() {
  // Configura a conexão com o servidor de produção
  const transport = new SSEClientTransport(
    new URL("https://mcp.apibrasil.cloud/mcp")
  );

  const client = new Client(
    { name: "meu-app-node", version: "1.0.0" },
    { capabilities: { tools: {} } }
  );

  console.log("Conectando...");
  await client.connect(transport);
  console.log("Conectado!");

  // Lista ferramentas
  const { tools } = await client.listTools();
  console.log("Ferramentas disponíveis:", tools.map(t => t.name));

  // Exemplo: Consultar CEP
  // Substitua pelos seus tokens reais
  try {
    const resultado = await client.callTool({
      name: "cep_lookup",
      arguments: {
        cep: "01001000",
        bearer: "SEU_BEARER_TOKEN",
        deviceToken: "SEU_DEVICE_TOKEN"
      }
    });
    console.log("Resultado:", JSON.stringify(resultado, null, 2));
  } catch (err) {
    console.error("Erro na chamada:", err.message);
  }
}

main();
```
