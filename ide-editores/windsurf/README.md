# Configuração para Windsurf (Codeium)

1. Vá em **Settings** ou procure por configurações MCP no painel lateral do Windsurf.
2. Adicione um novo servidor do tipo **Command**.
3. Configure os campos:

   - **Command:** `npx`
   - **Args:** `-y mcp-remote https://mcp.apibrasil.cloud/mcp --header "X-Apibrasil-Bearer:SEU_BEARER_TOKEN" --header "DeviceToken:SEU_DEVICE_TOKEN"`

4. Troque `SEU_BEARER_TOKEN` e `SEU_DEVICE_TOKEN` pelas suas credenciais da APIBrasil, salve e aguarde a conexão.

> [!NOTE]
> O servidor usa **Streamable HTTP**; a ponte [`mcp-remote`](https://www.npmjs.com/package/mcp-remote) converte o stdio/command do Windsurf para Streamable HTTP e injeta as credenciais via header.
