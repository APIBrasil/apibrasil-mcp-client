# Configuração para VS Code

Requer a extensão **MCP Servers** (ou compatível) instalada.

1. Abra o VS Code.
2. Abra as configurações de usuário em JSON:
   - Pressione `Ctrl+Shift+P` (ou `Cmd+Shift+P` no Mac).
   - Digite `Open User Settings (JSON)` e selecione.
3. Adicione ou edite o bloco `mcpServers` no arquivo `settings.json` com o conteúdo abaixo:

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

4. Salve o arquivo e reinicie o VS Code.
