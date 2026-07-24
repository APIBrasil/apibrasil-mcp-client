# Configuração para Supermaven e Outros Copilots

A maioria dos assistentes de código baseados em configuração local segue o padrão JSON.

1. Localize o arquivo de configuração do seu agente (consulte a documentação específica da ferramenta).
2. Adicione o servidor usando a ponte `npx` padrão:

```json
{
  "apibrasil": {
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
```

Troque `SEU_BEARER_TOKEN` e `SEU_DEVICE_TOKEN` pelas suas credenciais da APIBrasil.

> [!NOTE]
> O servidor usa **Streamable HTTP**; a ponte [`mcp-remote`](https://www.npmjs.com/package/mcp-remote) converte stdio ⇆ Streamable HTTP e injeta as credenciais via header.
