# Uso em Código (Node.js e Python)

Para integrações customizadas (bots, scripts, automações).

## Node.js

Use o `SSEClientTransport` do SDK oficial.

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { SSEClientTransport } from "@modelcontextprotocol/sdk/client/sse.js";
import { EventSource } from "eventsource"; // Necessário instalar: npm install eventsource

global.EventSource = EventSource;

const transport = new SSEClientTransport(new URL("https://mcp.apibrasil.cloud/mcp"));
const client = new Client({ name: "my-app", version: "1.0" }, { capabilities: {} });

await client.connect(transport);
// client.callTool(...)
```

## Python

Use o cliente MCP Python.

```python
# pip install mcp
from mcp.client.sse import sse_client

async with sse_client("https://mcp.apibrasil.cloud/mcp") as client:
    # Listar ferramentas
    tools = await client.list_tools()
    
    # Chamar ferramenta
    result = await client.call_tool("cep_lookup", arguments={
        "cep": "01001000", 
        "bearer": "SEU_TOKEN",
        "deviceToken": "SEU_DEVICE_TOKEN"
    })
```
