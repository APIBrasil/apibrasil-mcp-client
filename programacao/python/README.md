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
from mcp.client.sse import sse_client

async def main():
    url = "https://mcp.apibrasil.cloud/mcp"
    
    print(f"Conectando a {url}...")
    
    # Gerenciador de contexto conecta e desconecta automaticamente
    async with sse_client(url) as client:
        print("Conectado!")
        
        # 1. Listar Ferramentas
        tools_result = await client.list_tools()
        print("\nFerramentas disponíveis:")
        for tool in tools_result.tools:
            print(f"- {tool.name}")
            
        # 2. Chamar Ferramenta (Exemplo CEP)
        # Substitua pelos seus tokens
        try:
            result = await client.call_tool(
                name="cep_lookup",
                arguments={
                    "cep": "01001000",
                    "bearer": "SEU_BEARER_TOKEN",
                    "deviceToken": "SEU_DEVICE_TOKEN"
                }
            )
            print("\nResultado da consulta:")
            print(result)
        except Exception as e:
            print(f"\nErro ao chamar ferramenta: {e}")

if __name__ == "__main__":
    asyncio.run(main())
```
