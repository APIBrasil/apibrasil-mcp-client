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
        "mcp-remote",
        "https://mcp.apibrasil.cloud/mcp",
        "--header",
        "X-Apibrasil-Bearer:${APIBRASIL_BEARER}",
        "--header",
        "DeviceToken:${APIBRASIL_DEVICE_TOKEN}"
      ],
      "env": {
        "APIBRASIL_BEARER": "SEU_BEARER_TOKEN",
        "APIBRASIL_DEVICE_TOKEN": "SEU_DEVICE_TOKEN"
      }
    }
  }
}
```

3. Troque `SEU_BEARER_TOKEN` e `SEU_DEVICE_TOKEN` pelas suas credenciais da APIBrasil.
4. Reinicie o aplicativo Claude.

> [!NOTE]
> **Transporte:** o endpoint MCP da APIBrasil usa **Streamable HTTP**. O Claude Desktop só fala **stdio**, então usamos a ponte oficial [`mcp-remote`](https://www.npmjs.com/package/mcp-remote), que converte stdio ⇆ Streamable HTTP e injeta as credenciais via header. Detalhes em [`../../conceitos/credenciais/`](../../conceitos/credenciais/).
