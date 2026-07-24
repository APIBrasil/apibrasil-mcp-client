# Descoberta dinâmica

Três ferramentas cobrem **qualquer serviço** do gateway APIBrasil — inclusive os que ainda não têm tool dedicada. Por isso a lista de ferramentas pode ser enxuta: além das tools diretas mais usadas, estas três alcançam todo o resto do catálogo.

| Tool | Faz | Rota do gateway |
| :--- | :--- | :--- |
| `apibrasil_catalog` | Lista as APIs ativas (slug, serviço, preço) | `GET /api/v2/apis` |
| `apibrasil_describe` | Template do body de uma `action` | `GET /api/v2/endpoint/body` |
| `apibrasil_call` | Despacha `service` / `action` / `payload` | `ANY /api/v2/{service}/{action}` |

## Fluxo típico

```text
apibrasil_catalog          → descobre quais serviços/actions existem
      ↓
apibrasil_describe         → descobre o formato do payload de uma action
      ↓
apibrasil_call             → executa a chamada
```

Exemplo de `apibrasil_call`:

```json
{
  "name": "apibrasil_call",
  "arguments": {
    "service": "cep",
    "action": "cep",
    "payload": { "cep": "01001000" },
    "bearer": "SEU_BEARER_TOKEN",
    "deviceToken": "SEU_DEVICE_TOKEN"
  }
}
```

## Resources (não ocupam a lista de tools)

O catálogo também é exposto como **resource** — o client pode lê-lo sem gastar um slot de ferramenta:

| Resource | Conteúdo |
| :--- | :--- |
| `apibrasil://catalog` | Catálogo completo de APIs ativas. |
| `apibrasil://api/{slug}` | Detalhe de uma API específica (template de URI). |
| `apibrasil.docs` | Link para a documentação oficial. |

## Quando usar descoberta vs tool dedicada

- **Tool dedicada** (ex.: `cep_lookup`, `vehicles_consulta`): fluxos comuns, com schema tipado e validação. Prefira quando existir.
- **Descoberta** (`apibrasil_call`): serviços sem wrapper, endpoints novos, ou quando você quer um caminho único e genérico para tudo.
