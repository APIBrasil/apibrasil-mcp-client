# Configuração para Cursor IDE

## Método Recomendado (via Comando Ponte)

O Cursor conecta-se preferencialmente via comando local. Usaremos um adaptador para conectar ao servidor remoto.

1. Abra o Cursor.
2. Vá em **Cursor Settings** (ícone de engrenagem no canto superior direito ou `Ctrl+,`).
3. Navegue até **Features** > **MCP**.
4. Clique em **+ Add New MCP Server**.
5. Preencha os campos:

   - **Name:** `APIBrasil`
   - **Type:** `command`
   - **Command:** `npx`
   - **Args:** `-y @modelcontextprotocol/server-sse-client --url https://mcp.apibrasil.cloud/mcp`

6. Clique em **Add**. A luz verde deve acender indicando conexão.
