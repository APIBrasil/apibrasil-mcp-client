# Integração com Chainlit

Chainlit é um framework Python para construir interfaces de chat (tipo Streamlit para LLMs).

## Código (app.py)

Você precisa usar o SDK Python para conectar o Chainlit ao MCP.

```python
import chainlit as cl
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

URL = "https://mcp.apibrasil.cloud/mcp"

@cl.on_chat_start
async def start():
    # Conecta ao MCP via Streamable HTTP e lista as ferramentas
    async with streamablehttp_client(URL) as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await session.list_tools()
            await cl.Message(
                content=f"Conectado! {len(tools.tools)} ferramentas disponíveis."
            ).send()

@cl.on_message
async def main(message: cl.Message):
    # Lógica para decidir qual ferramenta chamar (usando um LLM)
    # ...
    pass
```
