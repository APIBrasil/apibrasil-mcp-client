# Integração com n8n

O n8n é uma ferramenta de automação de fluxo de trabalho poderosa. Este guia mostra como conectar a APIBrasil usando nós nativos de **HTTP Request**.

## 🚀 Como Usar (Importação Rápida)

1.  Baixe o arquivo [`workflow.json`](./workflow.json).
2.  No seu painel do n8n, vá em **Workflows** > **Import from File**.
3.  Selecione o arquivo baixado.

## 🔑 Configuração de Credenciais

Para que o fluxo funcione, você precisa configurar a autenticação:

1.  No n8n, vá em **Credentials** > **New**.
2.  Procure por **Header Auth**.
3.  Nomeie como `APIBrasil Auth`.
4.  Configuração:
    *   **Name**: `Authorization`
    *   **Value**: `Bearer SEU_TOKEN_AQUI`
5.  Salve.

> **Nota:** O `DeviceToken` também é necessário. No exemplo do workflow, ele está configurado para ler de uma variável de ambiente (`$env.APIBRASIL_DEVICE_TOKEN`) ou você pode inseri-lo manualmente no header do nó HTTP.

## 🛠️ Detalhes do Fluxo

O workflow de exemplo faz o seguinte:

1.  **Webhook Trigger**: Recebe um POST com JSON contendo `{ "cnpj": "...", "telefone_destino": "..." }`.
2.  **Consulta CNPJ**: Chama a APIBrasil (`/dados/cnpj/credits`) para buscar a Razão Social e Situação.
3.  **Envia WhatsApp**: Pega o retorno do CNPJ e envia uma mensagem formatada para o telefone informado via `/whatsapp/sendText`.

## 📦 Variáveis de Ambiente (Docker/Self-Hosted)

Se você roda o n8n via Docker, adicione estas variáveis ao seu `docker-compose.yml` para segurança máxima:

```yaml
environment:
  - APIBRASIL_TOKEN=seu_bearer_token_aqui
  - APIBRASIL_DEVICE_TOKEN=seu_device_token_aqui
```

Assim você pode usar `{{ $env.APIBRASIL_TOKEN }}` em qualquer lugar do fluxo.
