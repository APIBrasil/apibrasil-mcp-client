# Changelog

Todas as mudanças relevantes deste repositório. O formato segue, de forma
aproximada, [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/).

## [Unreleased]

### Corrigido
- **Ponte quebrada:** todas as configs apontavam para `@modelcontextprotocol/server-sse-client`, que **não existe no npm**. Substituído pela ponte oficial [`mcp-remote`](https://www.npmjs.com/package/mcp-remote) em todos os clientes, IDEs e READMEs.
- **Transporte:** documentação atualizada de "SSE" para **Streamable HTTP** (rótulo correto do servidor), incluindo a tabela TL;DR e as instruções de seleção de tipo nos clientes.
- **`package.json`:** era uma cópia do servidor (nome errado, `prepare: tsc` quebrava `npm i`). Reescrito como repositório de documentação (`private`, sem build).
- **Exemplos de código:** Node.js/Python migrados para `StreamableHTTPClientTransport` / `streamablehttp_client` + `ClientSession`; Go/Java/C#/n8n migrados do handshake HTTP+SSE legado para o fluxo Streamable HTTP (`initialize` → `Mcp-Session-Id` → `tools/call`).

### Adicionado
- **Credenciais** em todas as configs, injetadas por `env`/header através da ponte `mcp-remote`.
- Seção **[`conceitos/`](./conceitos/)**: credenciais, descoberta dinâmica e troubleshooting (402/403/410/422).
- **CI**: valida que os pacotes npm de ponte existem no registry (`scripts/check_mcp_packages.py`) e que os links relativos de markdown não estão quebrados (`scripts/check_links.py`).
- Governança: `SECURITY.md`, `CODEOWNERS`, templates de issue/PR.
- Índice auto-gerado agora lista páginas `.md` soltas (ex.: `vibe-coder/`).
- `README.en.md` (versão em inglês).

## [1.0.0]
- Base de conhecimento inicial: integrações para clientes de IA, IDEs, chatbots, low-code, cloud e linguagens de programação.
