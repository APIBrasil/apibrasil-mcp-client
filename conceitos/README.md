# Conceitos do MCP APIBrasil

Guias de referência sobre **como consumir** o endpoint MCP da APIBrasil — para além do "copie e cole a config". Leia estas páginas quando precisar autenticar, descobrir APIs dinamicamente ou depurar um erro.

| Página | Para quê |
| :--- | :--- |
| [Credenciais](./credenciais/) | Como passar `bearer` / `DeviceToken` / `SecretKey` (header ou argumento) e o token de transporte. |
| [Descoberta dinâmica](./descoberta/) | Fluxo `apibrasil_catalog` → `apibrasil_describe` → `apibrasil_call` e os resources. |
| [Troubleshooting](./troubleshooting/) | Erros do gateway (402/403/410/422), problemas de sessão e enganos comuns. |

> Endpoints: **MCP** `https://mcp.apibrasil.cloud/mcp` · **Gateway REST** `https://gateway.apibrasil.io/api/v2` · **Docs** [doc.apibrasil.io](https://doc.apibrasil.io).
