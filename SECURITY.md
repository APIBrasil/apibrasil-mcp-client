# Política de Segurança

## Reportando uma vulnerabilidade

Se você encontrar uma vulnerabilidade de segurança **neste repositório de documentação** (ex.: um exemplo que vaza credenciais, um snippet que induz a uma configuração insegura), por favor:

1. **Não** abra uma issue pública.
2. Envie um e-mail para **contato@apibrasil.com.br** com o assunto `SECURITY: apibrasil-mcp-client`.
3. Inclua o arquivo afetado e uma descrição do risco.

Responderemos o mais rápido possível.

> Para vulnerabilidades no **servidor MCP** ou no **gateway da APIBrasil**, use os canais do respectivo projeto / [doc.apibrasil.io](https://doc.apibrasil.io).

## Boas práticas ao contribuir

Este repositório contém **apenas configurações e exemplos**. Nunca comite segredos:

- Use sempre placeholders (`SEU_BEARER_TOKEN`, `SEU_DEVICE_TOKEN`) — nunca tokens reais.
- Prefira injetar credenciais por `env` ou header, não inline no código. Veja [`conceitos/credenciais/`](./conceitos/credenciais/).
- Se você acidentalmente commitou um token, **revogue-o imediatamente** no painel da APIBrasil e gere um novo.

## Escopo

| Em escopo | Fora de escopo |
| :--- | :--- |
| Exemplos que expõem/induzem vazamento de credenciais | Bugs do servidor MCP (repositório próprio) |
| Configurações inseguras recomendadas nas docs | Bugs do gateway REST da APIBrasil |
| Links para pacotes/hosts maliciosos | Vulnerabilidades de ferramentas de terceiros (VS Code, n8n, etc.) |
