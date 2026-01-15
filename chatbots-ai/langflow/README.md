# Integração com LangFlow

O LangFlow permite criar componentes customizados em Python.

## Criando um Componente MCP

1. Arraste um **Custom Component**.
2. Edite o código Python.
3. Use o código abaixo para conectar ao servidor MCP:

```python
from langflow import CustomComponent
from mcp.client.sse import sse_client
import asyncio

class MCPToolComponent(CustomComponent):
    display_name = "APIBrasil MCP"
    description = "Executa ferramentas via MCP"

    def build_config(self):
        return {
            "tool_name": {"display_name": "Nome da Tool", "value": "cep_lookup"},
            "arguments": {"display_name": "Argumentos (JSON)", "value": "{}"},
        }

    def build(self, tool_name: str, arguments: dict):
        async def run_mcp():
            url = "https://mcp.apibrasil.cloud/mcp"
            async with sse_client(url) as client:
                result = await client.call_tool(tool_name, arguments)
                return str(result)
        
        # Nota: LangFlow roda em loop assíncrono, pode precisar de ajustes
        return asyncio.run(run_mcp())
```
