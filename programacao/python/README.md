# Consumindo APIBrasil MCP com Python

Este exemplo usa o SDK oficial `mcp` para Python (asyncio).

## 1. Instalação

No seu ambiente virtual:

```bash
pip install mcp
```

## 2. Código (client.py)

```python
import asyncio
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

URL = "https://mcp.apibrasil.cloud/mcp"

# Opcional: enviar credenciais por header (ficam fora do contexto do modelo)
HEADERS = {
    "X-Apibrasil-Bearer": "SEU_BEARER_TOKEN",
    "DeviceToken": "SEU_DEVICE_TOKEN",
}


async def main():
    print(f"Conectando a {URL}...")

    # Streamable HTTP: o context manager entrega os streams de leitura/escrita
    async with streamablehttp_client(URL, headers=HEADERS) as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()
            print("Conectado!")

            # 1. Listar Ferramentas
            tools_result = await session.list_tools()
            print("\nFerramentas disponíveis:")
            for tool in tools_result.tools:
                print(f"- {tool.name}")

            # 2. Chamar Ferramenta (Exemplo CEP — a tool exige bearer e deviceToken)
            try:
                result = await session.call_tool(
                    name="cep_lookup",
                    arguments={
                        "cep": "01001000",
                        "bearer": "SEU_BEARER_TOKEN",
                        "deviceToken": "SEU_DEVICE_TOKEN",
                    },
                )
                print("\nResultado da consulta:")
                print(result)
            except Exception as e:
                print(f"\nErro ao chamar ferramenta: {e}")


if __name__ == "__main__":
    asyncio.run(main())
```
