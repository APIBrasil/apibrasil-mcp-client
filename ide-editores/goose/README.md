# Configuração para Goose (Block)

Goose é um agente de IA open-source para engenharia de software.

## Configuração

1. Vá em **Settings** > **Extensions**.
2. Selecione **Add Extension** > **MCP Server**.
3. Configure como **Stdio**:
   - **Name:** APIBrasil
   - **Command:** `npx`
   - **Arguments:** `-y @modelcontextprotocol/server-sse-client --url https://mcp.apibrasil.cloud/mcp`
4. Habilite a extensão.

O Goose agora poderá usar as ferramentas da APIBrasil para realizar tarefas complexas.
