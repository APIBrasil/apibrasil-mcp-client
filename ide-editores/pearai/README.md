# Configuração para PearAI

PearAI é um fork do VS Code focado em IA (similar ao Cursor), open-source.

## Configuração

1. Abra o painel de configurações (Settings).
2. Procure por **PearAI: MCP**.
3. Edite o arquivo de configuração `mcp.json` (ou similar, dependendo da versão).
4. Adicione:

```json
{
  "mcpServers": {
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
```

O formato é idêntico ao do VS Code padrão.
