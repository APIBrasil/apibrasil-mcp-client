# Prompt para Replit Agent: Bot Sommelier

Cria um bot de WhatsApp inteligente hospedado no Replit, combinando APIBrasil (WhatsApp) e OpenAI (Inteligência).

## Onde usar
**Replit Agent**.

## Prompt para Copiar

```markdown
Atue como um Engenheiro Python Backend.
Crie um Bot de WhatsApp usando Flask que recomenda vinhos.

Estrutura do Projeto:
1.  `main.py`: Servidor Flask.
2.  `services/whatsapp.py`: Módulo para envio de mensagens via APIBrasil.
3.  `services/ai.py`: Módulo para gerar recomendações via OpenAI.

Fluxo da Aplicação:
1.  Receba um POST no webhook `/webhook`.
2.  Valide se o payload é uma mensagem de texto recebida.
3.  Envie o texto do usuário para a OpenAI (GPT-4o-mini) com o system prompt: "Você é um sommelier experiente. Recomende um vinho para a ocasião descrita. Seja breve e elegante."
4.  Pegue a resposta da IA e envie para o usuário via APIBrasil (`/whatsapp/sendText`).

Requisitos Críticos:
-   **Segurança**: Use `os.environ` para pegar as chaves.
    -   `APIBRASIL_TOKEN`
    -   `DEVICE_TOKEN`
    -   `OPENAI_API_KEY`
    -   (Eu irei configurar essas chaves nos Secrets do Replit manualmente).
-   **Concorrência**: A rota do webhook deve responder `200 OK` imediatamente. O processamento da IA deve ser feito em background (use `threading` ou simples chamada assíncrona se o Flask permitir).

Dependências:
-   `flask`, `requests`, `openai`
```
