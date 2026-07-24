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

O formato é idêntico ao do VS Code padrão. Troque `SEU_BEARER_TOKEN` e `SEU_DEVICE_TOKEN` pelas suas credenciais da APIBrasil.

> [!NOTE]
> O servidor usa **Streamable HTTP**; a ponte [`mcp-remote`](https://www.npmjs.com/package/mcp-remote) converte stdio ⇆ Streamable HTTP e injeta as credenciais via header. Veja [`../../conceitos/credenciais/`](../../conceitos/credenciais/).
