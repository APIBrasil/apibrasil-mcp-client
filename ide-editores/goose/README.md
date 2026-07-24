# Configuração para Goose (Block)

Goose é um agente de IA open-source para engenharia de software.

## Configuração

1. Vá em **Settings** > **Extensions**.
2. Selecione **Add Extension** > **MCP Server**.
3. Configure como **Stdio**:
   - **Name:** APIBrasil
   - **Command:** `npx`
   - **Arguments:** `-y mcp-remote https://mcp.apibrasil.cloud/mcp --header "X-Apibrasil-Bearer:SEU_BEARER_TOKEN" --header "DeviceToken:SEU_DEVICE_TOKEN"`
4. Troque `SEU_BEARER_TOKEN` e `SEU_DEVICE_TOKEN` pelas suas credenciais da APIBrasil e habilite a extensão.

> [!NOTE]
> O servidor usa **Streamable HTTP**; a ponte [`mcp-remote`](https://www.npmjs.com/package/mcp-remote) converte o stdio do Goose para Streamable HTTP e injeta as credenciais via header.

O Goose agora poderá usar as ferramentas da APIBrasil para realizar tarefas complexas.
