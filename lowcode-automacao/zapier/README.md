# Integração com Zapier

## Via Webhooks by Zapier / Code by Zapier

### Opção 1: Code by Zapier (Python/JS)
O Zapier permite rodar scripts curtos.

**Limitação:** O tempo limite de execução é curto (poucos segundos). O handshake SSE + Chamada de Tool pode estourar esse tempo.

### Opção 2: Zapier AI Actions
Se você estiver usando o **Zapier Central** (plataforma de AI):
1. Adicione uma "Custom Action".
2. Aponte para a API REST da APIBrasil (`gateway.apibrasil.io`).

**Nota:** Atualmente o Zapier não consome servidores MCP diretamente. A integração recomendada é via endpoints REST tradicionais documentados em `https://doc.apibrasil.io`.
