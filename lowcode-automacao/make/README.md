# Integração com Make (Integromat)

O Make funciona via módulos HTTP. Assim como no n8n, conexões SSE persistentes não são nativas.

## Solução

Use o módulo **HTTP - Make a Request**.

1. **URL:** `https://gateway.apibrasil.io/api/v2/...` (Use a API direta).
   
*Por que não usar o endpoint MCP?*
Porque o Make espera uma resposta imediata (Request -> Response). O endpoint MCP `/mcp` é um stream infinito (SSE). O Make ficaria "pendurado" esperando o request terminar, consumindo operações até dar timeout.

**Conclusão para Make:**
Use este servidor MCP apenas se estiver usando o "AI Agent" do Make (se houver suporte futuro). Para fluxos de automação padrão, use a API REST direta da APIBrasil.
