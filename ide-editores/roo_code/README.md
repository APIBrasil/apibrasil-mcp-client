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
   - **Args:** `-y mcp-remote https://mcp.apibrasil.cloud/mcp --header "X-Apibrasil-Bearer:SEU_BEARER_TOKEN" --header "DeviceToken:SEU_DEVICE_TOKEN"`

5. Troque `SEU_BEARER_TOKEN` e `SEU_DEVICE_TOKEN` pelas suas credenciais da APIBrasil.
6. O Roo Code detectará automaticamente as ferramentas (`cep_lookup`, etc.) e as usará quando você pedir (ex: "Consulte o CEP 01001000").

> [!NOTE]
> O servidor usa **Streamable HTTP**; a ponte [`mcp-remote`](https://www.npmjs.com/package/mcp-remote) converte o stdio/command do Roo Code para Streamable HTTP e injeta as credenciais via header.
