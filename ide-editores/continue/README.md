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
            "mcp-remote",
            "https://mcp.apibrasil.cloud/mcp",
            "--header",
            "X-Apibrasil-Bearer:SEU_BEARER_TOKEN",
            "--header",
            "DeviceToken:SEU_DEVICE_TOKEN"
          ]
        }
      }
    ]
  }
}
```

3. Troque `SEU_BEARER_TOKEN` e `SEU_DEVICE_TOKEN` pelas suas credenciais da APIBrasil.
4. Reinicie a extensão/IDE.

> [!NOTE]
> O servidor usa **Streamable HTTP**; a ponte [`mcp-remote`](https://www.npmjs.com/package/mcp-remote) faz o `stdio` do Continue conversar com o endpoint remoto e injeta as credenciais via header. Veja [`../../conceitos/credenciais/`](../../conceitos/credenciais/).
