# Consumindo APIBrasil MCP com Node.js

Este exemplo usa o SDK oficial do MCP para TypeScript/Node.js.

## 1. Instalação

Abra seu terminal na pasta do projeto e instale as dependências:

```bash
npm install @modelcontextprotocol/sdk
```

## 2. Código (index.js ou index.ts)

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StreamableHTTPClientTransport } from "@modelcontextprotocol/sdk/client/streamableHttp.js";

async function main() {
  // O servidor APIBrasil usa o transporte Streamable HTTP.
  // Opcional: enviar as credenciais por header (ficam fora dos argumentos/logs).
  const transport = new StreamableHTTPClientTransport(
    new URL("https://mcp.apibrasil.cloud/mcp"),
    {
      requestInit: {
        headers: {
          "X-Apibrasil-Bearer": "SEU_BEARER_TOKEN",
          "DeviceToken": "SEU_DEVICE_TOKEN"
        }
      }
    }
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

  // Exemplo: Consultar CEP (a tool exige bearer e deviceToken como argumentos)
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
