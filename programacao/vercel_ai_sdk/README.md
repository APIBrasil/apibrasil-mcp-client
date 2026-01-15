# Integração com Vercel AI SDK (Next.js)

Ideal para criar Chatbots com React que usam suas ferramentas.

## Rota de API (app/api/chat/route.ts)

```typescript
import { openai } from '@ai-sdk/openai';
import { streamText, tool } from 'ai';
import { z } from 'zod';

export async function POST(req: Request) {
  const { messages } = await req.json();

  const result = streamText({
    model: openai('gpt-4-turbo'),
    messages,
    tools: {
      consultar_cep: tool({
        description: 'Consulta endereço por CEP',
        parameters: z.object({ cep: z.string() }),
        execute: async ({ cep }) => {
          // Chamada à APIBrasil
          const res = await fetch('https://gateway.apibrasil.io/api/v2/cep/cep', {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${process.env.APIBRASIL_TOKEN}`,
                'DeviceToken': `${process.env.APIBRASIL_DEVICE_TOKEN}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ cep })
          });
          return res.json();
        },
      }),
    },
  });

  return result.toDataStreamResponse();
}
```

O Vercel AI SDK abstrai a chamada da ferramenta, permitindo que o LLM decida quando chamar sua API.
