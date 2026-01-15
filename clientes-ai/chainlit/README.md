# Integração com Chainlit

Chainlit é um framework Python para construir interfaces de chat (tipo Streamlit para LLMs).

## Código (app.py)

Você precisa usar o SDK Python para conectar o Chainlit ao MCP.

```python
import chainlit as cl
from mcp.client.sse import sse_client

@cl.on_chat_start
async def start():
    # Conecta ao MCP
    url = "https://mcp.apibrasil.cloud/mcp"
    async with sse_client(url) as client:
        # Armazena o cliente na sessão
        cl.user_session.set("mcp_client", client)
        
        # Lista tools e registra como Actions do Chainlit
        tools = await client.list_tools()
        await cl.Message(content=f"Conectado! {len(tools.tools)} ferramentas disponíveis.").send()

@cl.on_message
async def main(message: cl.Message):
    # Lógica para decidir qual ferramenta chamar (usando um LLM)
    # ...
    pass
```
