# Integração com Stack AI

Stack AI permite construir workflows de LLM complexos.

## API Node

1. Arraste um nó **API** para o canvas.
2. **Method:** POST.
3. **URL:** `https://gateway.apibrasil.io/api/v2/cep/cep`.
4. **Headers:** Adicione Authorization e DeviceToken.
5. **Inputs:** Conecte o input do usuário ao campo `cep` do Body JSON.

## LLM + MCP (Via Code Node)
Se quiser usar o servidor MCP para manter o contexto, use um **Code Node (Python)** e implemente o cliente SSE (`mcp` library), similar ao exemplo do LangFlow.
