# Configuração para Continue (VS Code & JetBrains)

O **Continue** é a principal extensão open-source que traz suporte MCP para o JetBrains (IntelliJ, PyCharm) e VS Code.

## Configuração (`config.json`)

1. Abra o arquivo de configuração do Continue (`~/.continue/config.json`).
2. Adicione o bloco `experimental` com `modelContextProtocolServers`.

```json
{
  "experimental": {
    "modelContextProtocolServers": [
      {
        "transport": {
          "type": "stdio",
          "command": "npx",
          "args": [
            "-y",
            "@modelcontextprotocol/server-sse-client",
            "--url",
            "https://mcp.apibrasil.cloud/mcp"
          ]
        }
      }
    ]
  }
}
```

3. Reinicie a extensão/IDE.
