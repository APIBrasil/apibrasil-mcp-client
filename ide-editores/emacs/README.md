# Configuração para Emacs

Para usar MCP no Emacs, recomenda-se o pacote **`llm`** ou integrações customizadas com `gptel`.

## Exemplo com `gptel` + Script Ponte

O Emacs não tem um cliente MCP "plug-and-play" visual, mas pode interagir via funções.

1. Você deve rodar o cliente ponte localmente em um terminal:
   ```bash
   npx -y @modelcontextprotocol/server-sse-client --url https://mcp.apibrasil.cloud/mcp
   ```

2. Configure seu pacote LLM para reconhecer as ferramentas JSON disponíveis. (Configuração avançada, requer conhecimento de Elisp para mapear JSON-RPC para chamadas de função do Emacs).

*Recomendação:* Para usuários de Emacs, o uso via CLI (terminal dentro do Emacs) usando o cliente Python ou Node.js (pasta `../../programacao`) costuma ser mais eficiente até que plugins nativos amadureçam.
