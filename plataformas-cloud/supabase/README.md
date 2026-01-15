# Integração com Supabase Edge Functions

Execute via Deno.

## Código (`index.ts`)

```typescript
Deno.serve(async (req) => {
  const { cep } = await req.json();

  const response = await fetch('https://gateway.apibrasil.io/api/v2/cep/cep', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${Deno.env.get('APIBRASIL_TOKEN')}`,
      'DeviceToken': Deno.env.get('APIBRASIL_DEVICE_TOKEN'),
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ cep })
  });

  const data = await response.json();

  return new Response(JSON.stringify(data), {
    headers: { "Content-Type": "application/json" },
  });
})
```
