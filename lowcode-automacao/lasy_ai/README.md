# Integração com Lasy.ai (IA do Ruyter / Vibe Coding)

A **Lasy.ai** é uma plataforma geradora de código (Text-to-App). Como ela cria o código para você (geralmente em React, Node.js ou HTML/JS), você deve **pedir** para ela incluir a integração.

## Prompt para usar na Lasy.ai

Copie e cole este prompt no chat da Lasy quando for criar seu app:

> "Crie uma funcionalidade no meu app que se conecte à APIBrasil. Quero consultar um CEP. Use a seguinte API via requisição HTTP POST padrão (fetch):
>
> **URL:** `https://gateway.apibrasil.io/api/v2/cep/cep`
> **Headers:**
> - `Authorization`: Bearer SEU_TOKEN_AQUI
> - `DeviceToken`: SEU_DEVICE_TOKEN_AQUI
> - `Content-Type`: application/json
> **Body:** `{ 'cep': '01001000' }`
>
> Crie um formulário onde eu digito o CEP e ele mostra o resultado na tela."

---

## E o protocolo MCP?

Como a Lasy gera aplicativos finais (frontend/backend), é mais fácil e estável pedir para ela usar a **API REST direta** (gateway.apibrasil.io) do que tentar implementar o cliente MCP complexo (SSE) dentro do código gerado, a menos que você esteja criando um Agente de AI avançado.

Se você realmente quiser que a Lasy crie um **Agente MCP**, use este prompt:

> "Crie um script Node.js que use a biblioteca `@modelcontextprotocol/sdk`. Ele deve se conectar via SSEClientTransport na url `https://mcp.apibrasil.cloud/mcp` e listar as ferramentas disponíveis."

**Nota:** A Lasy pode não ter acesso a instalar pacotes npm complexos dependendo de onde o código vai rodar. A opção REST (primeira acima) é a mais garantida.
