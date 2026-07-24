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
}
```

4. Troque `SEU_BEARER_TOKEN` e `SEU_DEVICE_TOKEN` pelas suas credenciais da APIBrasil.

> [!NOTE]
> O servidor usa **Streamable HTTP**; a ponte [`mcp-remote`](https://www.npmjs.com/package/mcp-remote) converte stdio ⇆ Streamable HTTP e injeta as credenciais via header. Veja [`../../conceitos/credenciais/`](../../conceitos/credenciais/).
