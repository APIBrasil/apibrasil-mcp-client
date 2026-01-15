# Configuração para Roo Code (Antigo Cline)

Roo Code é um agente autônomo para VS Code que suporta MCP nativamente.

## Configuração

1. Abra o painel do **Roo Code** no VS Code.
2. Clique no ícone de **MCP Servers** (formato de plugue/servidor).
3. Clique em **Add New Server**.
4. Preencha:
   - **Name:** APIBrasil
   - **Type:** Command / Stdio
   - **Command:** `npx`
   - **Args:** `-y @modelcontextprotocol/server-sse-client --url https://mcp.apibrasil.cloud/mcp`

5. O Roo Code detectará automaticamente as ferramentas (`cep_lookup`, etc.) e as usará quando você pedir (ex: "Consulte o CEP 01001000").
