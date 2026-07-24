# Credenciais (bearer, DeviceToken, SecretKey)

A maioria das ferramentas da APIBrasil precisa de **credenciais** para funcionar. Sem elas, o cliente conecta ao endpoint MCP mas toda chamada tarifada falha (veja [Troubleshooting](../troubleshooting/)).

Há **duas formas** de fornecer as credenciais ao endpoint hospedado. Argumento explícito sempre vence o header.

## 1. Header (via ponte `mcp-remote`) — recomendado

Ao conectar via [`mcp-remote`](https://www.npmjs.com/package/mcp-remote), envie as credenciais por header. Assim o token **não trafega como argumento de tool** nem aparece nos logs de tool do client.

```json
{
  "mcpServers": {
    "apibrasil": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.apibrasil.cloud/mcp",
        "--header",
        "X-Apibrasil-Bearer:${APIBRASIL_BEARER}",
        "--header",
        "DeviceToken:${APIBRASIL_DEVICE_TOKEN}"
      ],
      "env": {
        "APIBRASIL_BEARER": "SEU_BEARER_TOKEN",
        "APIBRASIL_DEVICE_TOKEN": "SEU_DEVICE_TOKEN"
      }
    }
  }
}
```

> O `mcp-remote` expande `${APIBRASIL_BEARER}` a partir do bloco `env`. **Não use espaço** em volta do `:` no `--header` (`Nome:valor`).

| Header | Alternativa | Corresponde à credencial |
| :--- | :--- | :--- |
| `X-Apibrasil-Bearer` | `Authorization` | `bearer` |
| `DeviceToken` | `X-Apibrasil-Device-Token` | `deviceToken` |
| `SecretKey` | `X-Apibrasil-Secret-Key` | `secretKey` |

## 2. Argumento da tool

Você também pode passar `bearer`, `deviceToken` e `SecretKey` diretamente nos `arguments` da chamada. É o modo mais explícito e o que os exemplos de código em [`../../programacao/`](../../programacao/) usam:

```json
{
  "name": "cep_lookup",
  "arguments": {
    "cep": "01001000",
    "bearer": "SEU_BEARER_TOKEN",
    "deviceToken": "SEU_DEVICE_TOKEN"
  }
}
```

## Token de transporte (quando exigido)

Alguns acessos podem exigir um **token de transporte** para autenticar no próprio endpoint `/mcp` — separado das credenciais da APIBrasil. Nesse caso, envie um header `Authorization` a mais e mantenha as credenciais da API em `X-Apibrasil-Bearer`:

```
"--header", "Authorization:Bearer SEU_TOKEN_DE_TRANSPORTE"
```

## Segurança

- Nunca comite tokens reais. Use `env`/gerenciadores de segredo e mantenha placeholders (`SEU_BEARER_TOKEN`) no repositório.
- O token do login vem normalizado **sem** o prefixo `Bearer`, pronto para uso.
