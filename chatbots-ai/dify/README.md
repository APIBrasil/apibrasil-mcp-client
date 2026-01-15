# Integração com Dify.ai

O Dify aceita **API Extensions** ou **Tools** customizadas via OpenAPI/Swagger.

## Como configurar

Como o MCP usa JSON-RPC sobre SSE, ele não é uma API REST padrão Swagger.

1. **Recomendado:** Use a funcionalidade "Code-based Tool" do Dify (se você rodar o Dify self-hosted).
2. **Alternativa:** Crie um proxy simples (middleware) que converte REST (padrão Dify) para MCP.

### Middleware Exemplo (Python/Flask)
Crie um app pequeno que recebe POST do Dify `/api/run-tool` e internamente usa o cliente MCP Python para chamar `https://mcp.apibrasil.cloud/mcp`.

```python
# Seu Middleware
@app.route('/dify-hook', methods=['POST'])
async def run_tool():
    data = request.json
    # Conecta no MCP e executa
    # Retorna o resultado JSON pro Dify
```

Em breve, plataformas como Dify devem suportar o protocolo MCP nativamente nas configurações de "Model Providers" ou "Tools".
