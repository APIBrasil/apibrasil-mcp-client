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

4. Troque `SEU_BEARER_TOKEN` e `SEU_DEVICE_TOKEN` pelas suas credenciais da APIBrasil.
5. Salve o arquivo e reinicie o VS Code.

> [!NOTE]
> O servidor usa **Streamable HTTP**; a ponte [`mcp-remote`](https://www.npmjs.com/package/mcp-remote) converte stdio ⇆ Streamable HTTP e injeta as credenciais via header. Veja [`../../conceitos/credenciais/`](../../conceitos/credenciais/).
