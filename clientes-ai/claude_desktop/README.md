# Configuração para Claude Desktop App

## Localização do Arquivo de Configuração

- **Mac:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

## Passo a Passo

1. Abra o arquivo de configuração acima (crie se não existir).
2. Cole o conteúdo do arquivo `claude_desktop_config.json` desta pasta:

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

3. Reinicie o aplicativo Claude.
