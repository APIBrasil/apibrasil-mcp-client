# Configuração para Zed Editor

1. Abra o Zed.
2. Abra as configurações do projeto ou globais (geralmente `.zed/settings.json` ou `Cmd+,`).
3. Adicione o bloco de configuração MCP:

```json
{
  "mcp": {
    "servers": {
      "apibrasil": {
        "command": "npx",
        "args": [
          "-y",
          "@modelcontextprotocol/server-sse-client",
          "--url",
          "https://mcp.apibrasil.cloud/mcp"
        ]
      }
    }
  }
}
```
