# Troubleshooting

O endpoint MCP **preserva o status HTTP semântico do gateway** e o transforma em um resultado `isError` com a mensagem original e uma dica acionável — em vez de um `HTTP 402` opaco.

## Erros do gateway

| Status | Significado | O que fazer |
| :--- | :--- | :--- |
| **402** | Sem saldo para a consulta | Recarregue créditos. O gateway já responde com o valor exato da consulta. Em **plano** (cobrança por `DeviceToken`), confira o dispositivo. |
| **403** | `DeviceToken` inválido ou IP não autorizado | Verifique o `DeviceToken` e a whitelist de IP da conta. |
| **410** | Rota morta (endpoint descontinuado) | A action mudou de nome/caminho. Use [`apibrasil_catalog`](../descoberta/) para achar a rota atual. |
| **422** | Falha de validação do payload | Cheque os campos com [`apibrasil_describe`](../descoberta/); algum obrigatório está faltando ou malformado. |

## Conexão e sessão

| Sintoma | Causa provável | Correção |
| :--- | :--- | :--- |
| `npm error 404 ... server-sse-client` | Pacote-ponte inexistente | Use `mcp-remote` (veja qualquer config deste repo). |
| Client conecta mas **nenhuma tool aparece** | Handshake incompleto | Confirme a URL `https://mcp.apibrasil.cloud/mcp` e, em clients nativos, selecione **Streamable HTTP**. |
| `401 / Unauthorized` no `/mcp` | Seu acesso exige token de transporte | Envie um header `Authorization: Bearer SEU_TOKEN_DE_TRANSPORTE`. Veja [Credenciais](../credenciais/). |
| Ferramenta retorna 402/403 mesmo "conectado" | Faltam credenciais da API | O transporte conectou, mas a tool precisa de `bearer`/`DeviceToken`. Veja [Credenciais](../credenciais/). |
| Timeout em n8n / Make / Zapier | Ambiente stateless matando o stream | Use a API REST direta (`gateway.apibrasil.io`) nessas plataformas. |

## Enganos comuns

- **Confundir os dois tokens.** O token de transporte (header `Authorization`, quando exigido) protege o *acesso ao endpoint MCP*; `bearer`/`DeviceToken` autenticam na *APIBrasil*. São independentes.
- **Rota errada de crédito.** Prefira a genérica `consulta_credits` (rota canônica `/consulta/{service}/credits`) aos wrappers legados marcados como *deprecated*.
- **Transporte legado.** O servidor é **Streamable HTTP**, não o antigo HTTP+SSE. Não faça `GET /mcp` esperando um evento `endpoint` — faça `POST` do `initialize` e leia o header `Mcp-Session-Id`.

## Testando por fora (curl)

```bash
# 1. initialize — copie o header Mcp-Session-Id da resposta
curl -i https://mcp.apibrasil.cloud/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":"init","method":"initialize","params":{"protocolVersion":"2025-06-18","clientInfo":{"name":"curl","version":"0.0.0"},"capabilities":{}}}'

# 2. tools/list — usando o Mcp-Session-Id obtido acima
curl -s https://mcp.apibrasil.cloud/mcp \
  -H "Content-Type: application/json" \
  -H "Mcp-Session-Id: SEU_SESSION_ID" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}'
```
