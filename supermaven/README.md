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
      "@modelcontextprotocol/server-sse-client",
      "--url",
      "https://mcp.apibrasil.cloud/mcp"
    ]
  }
}
```
