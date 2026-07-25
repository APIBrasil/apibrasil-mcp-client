# APIBrasil MCP Client

<img src="./assets/banner.svg" width="100%" alt="APIBrasil MCP Banner">

![Version](https://img.shields.io/badge/version-1.0.0-blue?style=flat-square) ![Protocol](https://img.shields.io/badge/protocol-MCP-success?style=flat-square) ![API](https://img.shields.io/badge/API-v2-orange?style=flat-square) [![smithery badge](https://smithery.ai/badge/apibrasil/gate)](https://smithery.ai/servers/apibrasil/gate)

**🌐 Idioma:** **Português** · [English](./README.en.md)

Base de conhecimento, configurações e guias para consumir o servidor **MCP** da APIBrasil em **clientes de IA**, **IDEs**, **chatbots** e **ferramentas de automação**.

> **Nota:** A [APIBrasil](https://apibrasil.io) é um Gateway de APIs unificado para dados nacionais (CEP, CNPJ, Veículos, etc). Este repositório foca na integração dessas APIs via **Protocolo MCP** para Agentes de Inteligência Artificial.

---

## Decisão Rápida (TL;DR)

Escolha o método de conexão baseado na natureza da sua plataforma:

| Característica | Protocolo MCP  | API REST  |
| :--- | :--- | :--- |
| **Protocolo** | Streamable HTTP (streaming) | HTTP Standard |
| **Estado** | **Stateful** (Sessão Persistente) | **Stateless** (Request/Response) |
| **Uso Ideal** | Cursor, Claude, Agentes de IA | n8n, Typebot, Zapier, Webhooks |
| **Vantagem** | Contexto contínuo para LLMs | Simplicidade e compatibilidade universal |

## Endpoints

> Utilize estes endereços para configurar seus clientes.

| Serviço | URL | Status |
| :--- | :--- | :--- |
| **MCP Server** | `https://mcp.apibrasil.cloud/mcp` | <img src="https://img.shields.io/badge/Online-green?style=flat-square" height="20"> |
| **API Gateway** | `https://gateway.apibrasil.io/api/v2` | <img src="https://img.shields.io/badge/Online-green?style=flat-square" height="20"> |
| **Docs** | [doc.apibrasil.io](https://doc.apibrasil.io) | <img src="https://img.shields.io/badge/Docs-blue?style=flat-square" height="20"> |

## Comece por aqui

Selecione o seu caso de uso para ir direto à documentação específica:

| Objetivo | Diretório | Descrição |
| :--- | :--- | :--- |
| **Conectar IA** | [`clientes-ai/`](./clientes-ai/) | Claude Desktop, LibreChat, Lovable |
| **Configurar IDE** | [`ide-editores/`](./ide-editores/) | VS Code, Cursor, Zed, JetBrains |
| **Criar Chatbot** | [`chatbots-ai/`](./chatbots-ai/) | Typebot, Flowise, LangFlow, Dify |
| **Automação** | [`lowcode-automacao/`](./lowcode-automacao/) | n8n, Make, Zapier, Bubble |
| **Programar** | [`programacao/`](./programacao/) | Python, Node.js, Go, Java, C# |
| **Entender o MCP** | [`conceitos/`](./conceitos/) | Credenciais, descoberta, troubleshooting |

## Configurações Rápidas (Snippets)

Copie e cole as configurações abaixo diretamente no seu arquivo de preferência.

### JSON Configs
- **Claude Desktop**: [`claude_desktop_config.json`](./clientes-ai/claude_desktop_config.json)
- **VS Code**: [`settings.json`](./ide-editores/vscode/settings.json)
- **Zed Editor**: [`settings.json`](./ide-editores/zed/settings.json)

### CLI Bridge (Ponte Local)
Para conectar via terminal ou clientes que só aceitam comandos `stdio`, use a ponte oficial [`mcp-remote`](https://www.npmjs.com/package/mcp-remote), que converte `stdio` ⇆ **Streamable HTTP** e injeta as credenciais por header:

```bash
npx -y mcp-remote https://mcp.apibrasil.cloud/mcp \
  --header "X-Apibrasil-Bearer:SEU_BEARER_TOKEN" \
  --header "DeviceToken:SEU_DEVICE_TOKEN"
```

> Como passar credenciais em cada cliente (header, `env` ou argumento): veja [`conceitos/credenciais/`](./conceitos/credenciais/).

### Exemplo REST (PowerShell)
Para testes rápidos de conectividade sem depender do protocolo MCP:

```powershell
$headers = @{
  Authorization = "Bearer SEU_BEARER_TOKEN"
  DeviceToken   = "SEU_DEVICE_TOKEN"
}

$body = @{ cep = "01001000" } | ConvertTo-Json

Invoke-RestMethod -Method Post `
  -Uri "https://gateway.apibrasil.io/api/v2/cep/cep" `
  -Headers $headers `
  -ContentType "application/json" `
  -Body $body
```

> [!IMPORTANT]
> **Segurança e Estado**
> 
> *   **Stateful:** O MCP mantém uma sessão ativa (`Mcp-Session-Id`) via **Streamable HTTP**. Não tente usá-lo em ambientes que matam a conexão imediatamente (como Serverless Functions puras sem stream).
> *   **Tokens:** Jamais comite seus tokens reais no repositório. Utilize variáveis de ambiente ou gerenciadores de segredos.

## Mapa do Repositório

Esta seção é otimizada para indexação e navegação rápida.

#### Índice por categoria (auto-gerado)

<!-- BEGIN:AUTO_INDEX -->
- **[assets](./assets)**

- **[chatbots-ai](./chatbots-ai)**
  - [Integração com Typebot](./chatbots-ai/README.md) — O Typebot executa fluxos rápidos e stateless. O protocolo MCP (que é stateful via Streamable HTTP) não é ideal para conexão direta via blocos nativos HTTP do...
  - [Integração com Botpress](./chatbots-ai/botpress/README.md) — No Botpress Studio, adicione um card **Execute Code** no seu fluxo.
  - [Integração com Dify.ai](./chatbots-ai/dify/README.md) — O Dify aceita **API Extensions** ou **Tools** customizadas via OpenAPI/Swagger.
  - [Integração com Flowise](./chatbots-ai/flowise/README.md) — O Flowise é uma ferramenta Low-Code para construir LLM Apps e suporta integração via **Custom Tools**.
  - [Integração com LangFlow](./chatbots-ai/langflow/README.md) — O LangFlow permite criar componentes customizados em Python.
  - [Integração com OpenAI GPTs (Custom Actions)](./chatbots-ai/openai_gpts/README.md) — Para conectar seu GPT personalizado à APIBrasil, você deve configurar uma **Action** usando o esquema OpenAPI (Swagger).
  - [Integração com Stack AI](./chatbots-ai/stack_ai/README.md) — Stack AI permite construir workflows de LLM complexos.
  - [Integração com Voiceflow](./chatbots-ai/voiceflow/README.md) — 1. Arraste um bloco **API** para o canvas.

- **[clientes-ai](./clientes-ai)**
  - [Configuração para Claude Desktop App](./clientes-ai/README.md) — - **Mac:** `~/Library/Application Support/Claude/claude_desktop_config.json`
  - [`claude_desktop_config.json`](./clientes-ai/claude_desktop_config.json)
  - [Integração com 5ire](./clientes-ai/5ire/README.md) — 5ire é um assistente focado em produtividade e blockchain, mas com suporte a ferramentas customizadas.
  - [Integração com AIaW (AI as Workspace)](./clientes-ai/aiaw/README.md) — 1. No painel de controle, vá em **Data Sources**.
  - [Integração com Chainlit](./clientes-ai/chainlit/README.md) — Chainlit é um framework Python para construir interfaces de chat (tipo Streamlit para LLMs).
  - [Configuração para ChatMCP](./clientes-ai/chatmcp/README.md) — Um cliente open-source focado puramente em testar e usar servidores MCP.
  - [Configuração para Cherry Studio](./clientes-ai/cherry_studio/README.md) — Cherry Studio é um cliente desktop elegante para múltiplos modelos.
  - [Configuração para Claude Desktop App](./clientes-ai/claude_desktop/README.md) — - **Mac:** `~/Library/Application Support/Claude/claude_desktop_config.json`
  - [Configuração para Glue AI](./clientes-ai/glue/README.md) — Glue é uma plataforma de chat para times com suporte a Agentes.
  - [Configuração para HyperChat](./clientes-ai/hyperchat/README.md) — HyperChat é um cliente desktop nativo para macOS/Windows.
  - [Configuração para LangDock](./clientes-ai/langdock/README.md) — LangDock é uma plataforma enterprise para LLMs.
  - [Configuração para LibreChat](./clientes-ai/librechat/README.md) — O LibreChat suporta conexões MCP remotas nativas (transporte `streamable-http`), facilitando a integração.
  - [Configuração para Lovable.dev](./clientes-ai/lovable/README.md) — O Lovable conecta-se nativamente via HTTPS (Streamable HTTP), sem necessidade de adaptadores.
  - [Configuração para MindPal](./clientes-ai/mindpal/README.md) — MindPal é um cliente web focado em fluxos visuais.
  - [Configuração via Smithery.ai](./clientes-ai/smithery/README.md) — Se o servidor estiver publicado no Smithery registry:
  - [Configuração para TypingMind](./clientes-ai/typingmind/README.md) — TypingMind é uma interface web popular para ChatGPT/Claude que suporta plugins.

- **[conceitos](./conceitos)**
  - [Conceitos do MCP APIBrasil](./conceitos/README.md) — Guias de referência sobre **como consumir** o endpoint MCP da APIBrasil — para além do "copie e cole a config". Leia estas páginas quando precisar autenticar...
  - [Credenciais (bearer, DeviceToken, SecretKey)](./conceitos/credenciais/README.md) — A maioria das ferramentas da APIBrasil precisa de **credenciais** para funcionar. Sem elas, o cliente conecta ao endpoint MCP mas toda chamada tarifada falha...
  - [Descoberta dinâmica](./conceitos/descoberta/README.md) — Três ferramentas cobrem **qualquer serviço** do gateway APIBrasil — inclusive os que ainda não têm tool dedicada. Por isso a lista de ferramentas pode ser en...
  - [Troubleshooting](./conceitos/troubleshooting/README.md) — O endpoint MCP **preserva o status HTTP semântico do gateway** e o transforma em um resultado `isError` com a mensagem original e uma dica acionável — em vez...

- **[ide-editores](./ide-editores)**
  - [Configuração para Cursor IDE](./ide-editores/README.md) — O Cursor conecta-se preferencialmente via comando local. Usaremos um adaptador para conectar ao servidor remoto.
  - [Configuração para Continue (VS Code & JetBrains)](./ide-editores/continue/README.md) — O **Continue** é a principal extensão open-source que traz suporte MCP para o JetBrains (IntelliJ, PyCharm) e VS Code.
  - [Configuração para Cursor IDE](./ide-editores/cursor/README.md) — O Cursor conecta-se preferencialmente via comando local. Usaremos um adaptador para conectar ao servidor remoto.
  - [Configuração para Emacs](./ide-editores/emacs/README.md) — Para usar MCP no Emacs, recomenda-se o pacote **`llm`** ou integrações customizadas com `gptel`.
  - [Configuração para Goose (Block)](./ide-editores/goose/README.md) — Goose é um agente de IA open-source para engenharia de software.
  - [Configuração para JetBrains (IntelliJ, PyCharm, WebStorm)](./ide-editores/jetbrains/README.md) — Atualmente, o suporte nativo a MCP no JetBrains ainda está em desenvolvimento por parte da JetBrains AI.
  - [Configuração para PearAI](./ide-editores/pearai/README.md) — PearAI é um fork do VS Code focado em IA (similar ao Cursor), open-source.
  - [Configuração para Roo Code (Antigo Cline)](./ide-editores/roo_code/README.md) — Roo Code é um agente autônomo para VS Code que suporta MCP nativamente.
  - [Configuração para Supermaven e Outros Copilots](./ide-editores/supermaven/README.md) — A maioria dos assistentes de código baseados em configuração local segue o padrão JSON.
  - [Configuração para VS Code](./ide-editores/vscode/README.md) — Requer a extensão **MCP Servers** (ou compatível) instalada. ([settings](./ide-editores/vscode/settings.json))
  - [Configuração para Windsurf (Codeium)](./ide-editores/windsurf/README.md) — 1. Vá em **Settings** ou procure por configurações MCP no painel lateral do Windsurf.
  - [Configuração para Zed Editor](./ide-editores/zed/README.md) — 1. Abra o Zed. ([settings](./ide-editores/zed/settings.json))

- **[lowcode-automacao](./lowcode-automacao)**
  - [Integração com n8n](./lowcode-automacao/README.md) — O n8n pode consumir o servidor MCP de duas formas: usando o nó **HTTP Request** (para chamadas manuais) ou o nó **Code** (para lidar com o handshake Streamab...
  - [Integração com ActivePieces](./lowcode-automacao/activepieces/README.md) — ActivePieces é uma alternativa open-source ao Zapier/n8n.
  - [Integração com Bubble.io](./lowcode-automacao/bubble/README.md) — O Bubble conecta-se via **API Connector**.
  - [Integração com FlutterFlow](./lowcode-automacao/flutterflow/README.md) — 1. No menu esquerdo, vá em **API Calls**.
  - [Integração com Google Sheets (Apps Script)](./lowcode-automacao/google_sheets/README.md) — Automatize planilhas com scripts customizados.
  - [Integração com Lasy.ai (IA do Ruyter / Vibe Coding)](./lowcode-automacao/lasy_ai/README.md) — A **Lasy.ai** é uma plataforma geradora de código (Text-to-App). Como ela cria o código para você (geralmente em React, Node.js ou HTML/JS), você deve **pedi...
  - [Integração com Make (Integromat)](./lowcode-automacao/make/README.md) — O Make funciona via módulos HTTP. Assim como no n8n, sessões MCP com stream persistente não são nativas.
  - [Integração com n8n](./lowcode-automacao/n8n/README.md) — O n8n é uma ferramenta de automação de fluxo de trabalho poderosa. Este guia mostra como conectar a APIBrasil usando nós nativos de **HTTP Request**.
  - [Integração com Microsoft Power Automate](./lowcode-automacao/power_automate/README.md) — 1. Vá em **Data** > **Custom Connectors**.
  - [Integração com Retool](./lowcode-automacao/retool/README.md) — Retool é ideal para painéis internos.
  - [Integração com Zapier](./lowcode-automacao/zapier/README.md) — O Zapier permite rodar scripts curtos.

- **[plataformas-cloud](./plataformas-cloud)**
  - [Integração com AWS Lambda](./plataformas-cloud/aws/README.md) — Para usar com Bedrock Agents, defina um **Action Group** com o schema OpenAPI da APIBrasil.
  - [Integração com Azure Functions](./plataformas-cloud/azure/README.md) — Use a funcionalidade "Add your data" ou Function Calling conectando a este endpoint.
  - [Integração com Cloudflare Workers](./plataformas-cloud/cloudflare/README.md)
  - [Integração com Discord (Discord.js)](./plataformas-cloud/discord/README.md)
  - [Integração com Google Cloud (Cloud Functions)](./plataformas-cloud/google_cloud/README.md) — Se estiver usando o Vertex AI, adicione a APIBrasil como uma **OpenAPI Tool** importando o schema JSON (similar ao exemplo do OpenAI GPTs).
  - [Integração com Salesforce (Apex)](./plataformas-cloud/salesforce/README.md) — Use Callouts para conectar ao Gateway APIBrasil.
  - [Integração com Slack (Bolt.js)](./plataformas-cloud/slack/README.md) — Crie um bot Slack que consulta a APIBrasil.
  - [Integração com Supabase Edge Functions](./plataformas-cloud/supabase/README.md) — Execute via Deno.
  - [Integração com Telegram (Telegraf)](./plataformas-cloud/telegram/README.md)
  - [Integração com Vercel (Serverless Functions)](./plataformas-cloud/vercel/README.md) — Exemplo de uma Serverless Function em Node.js que consome a APIBrasil.

- **[programacao](./programacao)**
  - [Consumindo APIBrasil MCP com C# (.NET)](./programacao/README.md) — Exemplo usando `HttpClient`.
  - [Consumindo APIBrasil MCP com Go (Golang)](./programacao/go/README.md) — Exemplo básico usando `net/http`.
  - [Consumindo APIBrasil MCP com Java](./programacao/java/README.md) — Exemplo usando Java 11+ (HttpClient nativo). Como não há SDK oficial estável para Java ainda, falamos o protocolo Streamable HTTP manualmente (POST de mensag...
  - [Consumindo APIBrasil MCP com Node.js](./programacao/nodejs/README.md) — Este exemplo usa o SDK oficial do MCP para TypeScript/Node.js.
  - [Consumindo APIBrasil MCP com PHP](./programacao/php/README.md) — Exemplo usando **Guzzle**, o cliente HTTP mais popular do ecossistema PHP (padrão no Laravel).
  - [Consumindo APIBrasil MCP com Python](./programacao/python/README.md) — Este exemplo usa o SDK oficial `mcp` para Python (asyncio).
  - [Consumindo APIBrasil MCP com Ruby](./programacao/ruby/README.md) — Exemplo usando a biblioteca padrão `net/http`.
  - [Consumindo APIBrasil MCP com Rust](./programacao/rust/README.md) — Exemplo usando **Tokio** (runtime assíncrono) e **Reqwest**.
  - [Consumindo APIBrasil via Terminal (cURL)](./programacao/shell/README.md) — A maneira mais rápida de testar endpoints.
  - [Consumindo APIBrasil MCP com Swift](./programacao/swift/README.md) — Exemplo nativo para iOS/macOS usando `URLSession` e `async/await`.
  - [Integração com Vercel AI SDK (Next.js)](./programacao/vercel_ai_sdk/README.md) — Ideal para criar Chatbots com React que usam suas ferramentas.

- **[vibe-coder](./vibe-coder)**
  - [Dashboard de Vendas com Envio de WhatsApp](./vibe-coder/01-dashboard-whatsapp.md) — Este exemplo cria um painel administrativo. O objetivo é visualizar vendas e enviar comprovantes para clientes via WhatsApp com um clique.
  - [Formulário Inteligente (CEP e CPF)](./vibe-coder/02-form-inteligente.md) — Este exemplo cria um formulário de cadastro de alta conversão que preenche o endereço automaticamente pelo CEP e valida o CPF em tempo real.
  - [Bot de Rastreio de Encomendas](./vibe-coder/03-bot-rastreio.md) — Script profissional em Node.js para monitorar encomendas e notificar via WhatsApp. Ideal para e-commerce ou uso pessoal.
  - [App de Consulta Veicular (Sinesp/Detran)](./vibe-coder/04-consulta-veicular.md) — Prompt para criar uma interface mobile moderna para consulta de placas, focada em utilidade e rapidez.
  - [Bot de Agendamento Inteligente (Webhook)](./vibe-coder/05-bot-agendamento.md) — Um servidor intermediário (Middleware) que recebe mensagens do WhatsApp, processa intenções básicas e responde.
  - [Disparo em Massa Inteligente (Python)](./vibe-coder/06-disparo-massa.md) — Script Python para envio de mensagens em massa com foco em segurança (anti-ban), logs detalhados e retomada de falhas.
  - [Enriquecimento de Dados (CRM CLI)](./vibe-coder/07-crm-enrichment.md) — Ferramenta de linha de comando (CLI) profissional para consultar e enriquecer dados de empresas (B2B) usando CNPJ.
  - [Bot de Previsão do Tempo (Cron)](./vibe-coder/08-clima-bot.md) — Serviço "Wake-up Call" que envia a previsão do tempo para uma lista de VIPs todas as manhãs.
  - [Verificador de Dias Úteis (Smart Calendar)](./vibe-coder/09-verificador-feriados.md) — Módulo utilitário para verificar se uma data é dia útil, considerando fins de semana e feriados nacionais (via API). Inclui sistema de Cache em memória para...
  - [Monitor de Saldo (Dashboard Pessoal)](./vibe-coder/10-monitor-saldo.md) — Uma ferramenta visual simples (HTML/JS) para verificar seu saldo e créditos na APIBrasil.
  - [Prompt para V0.dev: Central de Comunicação (CRM de WhatsApp)](./vibe-coder/11-prompt-v0-dev.md) — Prompt otimizado para gerar uma interface de chat profissional (estilo Intercom/Zendesk) pronta para conectar com a APIBrasil.
  - [Prompt para Bolt.new: SaaS de KYC (Validação Cadastral)](./vibe-coder/12-prompt-bolt-new.md) — Prompt para criar um SaaS completo de verificação de identidade usando a stack moderna do Bolt.
  - [Prompt para Replit Agent: Bot Sommelier](./vibe-coder/13-prompt-replit-agent.md) — Cria um bot de WhatsApp inteligente hospedado no Replit, combinando APIBrasil (WhatsApp) e OpenAI (Inteligência).
  - [App Streamlit: Consulta FIPE Profissional](./vibe-coder/14-script-streamlit.md) — Interface de dados rápida para consulta de preços de veículos.
  - [Webhook Bridge (Cloudflare Worker)](./vibe-coder/15-webhook-bridge.md) — Middleware serverless para conectar serviços externos (Stripe, Typeform) ao WhatsApp da APIBrasil.
<!-- END:AUTO_INDEX -->

<details>
<summary><strong>📂 Estrutura de Pastas (Navegação)</strong></summary>
<br>

<!-- BEGIN:REPO_TREE -->
```text
apibrasil-mcp-client
├── assets
├── chatbots-ai
│   ├── botpress
│   ├── dify
│   ├── flowise
│   ├── langflow
│   ├── openai_gpts
│   ├── stack_ai
│   └── voiceflow
├── clientes-ai
│   ├── 5ire
│   ├── aiaw
│   ├── chainlit
│   ├── chatmcp
│   ├── cherry_studio
│   ├── claude_desktop
│   ├── glue
│   ├── hyperchat
│   ├── langdock
│   ├── librechat
│   ├── lovable
│   ├── mindpal
│   ├── smithery
│   └── typingmind
├── conceitos
│   ├── credenciais
│   ├── descoberta
│   └── troubleshooting
├── ide-editores
│   ├── continue
│   ├── cursor
│   ├── emacs
│   ├── goose
│   ├── jetbrains
│   ├── pearai
│   ├── roo_code
│   ├── supermaven
│   ├── vscode
│   ├── windsurf
│   └── zed
├── lowcode-automacao
│   ├── activepieces
│   ├── bubble
│   ├── flutterflow
│   ├── google_sheets
│   ├── lasy_ai
│   ├── make
│   ├── n8n
│   ├── power_automate
│   ├── retool
│   └── zapier
├── plataformas-cloud
│   ├── aws
│   ├── azure
│   ├── cloudflare
│   ├── discord
│   ├── google_cloud
│   ├── salesforce
│   ├── slack
│   ├── supabase
│   ├── telegram
│   └── vercel
├── programacao
│   ├── go
│   ├── java
│   ├── nodejs
│   ├── php
│   ├── python
│   ├── ruby
│   ├── rust
│   ├── shell
│   ├── swift
│   └── vercel_ai_sdk
└── vibe-coder
```
<!-- END:REPO_TREE -->

</details>

<br>

Para atualizar o índice auto-gerado e a árvore depois de criar/remover pastas: `python scripts/update_readme_tree.py`.

## Termos de Busca (Tags)

> [!TIP]
> Utilize estes termos para localizar rapidamente configurações específicas dentro dos arquivos.

| Contexto | Termo de Busca |
| :--- | :--- |
| **Endpoint MCP** | `mcp.apibrasil.cloud/mcp` |
| **Ponte NPX** | `mcp-remote` |
| **Config JSON** | `mcpServers` |
| **Config Zed** | `"mcp": { "servers": ... }` |
| **Gateway REST** | `gateway.apibrasil.io/api/v2` |

## Contribuindo

Quer adicionar uma nova ferramenta ou corrigir algo?

👉 **[Leia nosso Guia de Contribuição](./CONTRIBUTING.md)**

Para manter o índice atualizado, lembre-se de rodar o script antes de commitar:

```bash
python scripts/update_readme_tree.py
```
