# Consumindo APIBrasil via Terminal (cURL)

A maneira mais rápida de testar endpoints.

## 1. Comando Direto

```bash
curl -X POST https://gateway.apibrasil.io/api/v2/cep/cep \
  -H "Authorization: Bearer SEU_TOKEN" \
  -H "DeviceToken: SEU_DEVICE" \
  -H "Content-Type: application/json" \
  -d '{"cep": "01001000"}'
```

## 2. Script Reutilizável (test_api.sh)

Crie um arquivo `.env` para não expor seus tokens no histórico do terminal.

```bash
#!/bin/bash

# Carrega variáveis
if [ -f .env ]; then
  export $(cat .env | xargs)
fi

TOKEN=${APIBRASIL_TOKEN:-"SEU_TOKEN_PADRAO"}
DEVICE=${APIBRASIL_DEVICE_TOKEN:-"SEU_DEVICE_PADRAO"}

echo "🚀 Consultando APIBrasil..."

curl -s -X POST https://gateway.apibrasil.io/api/v2/cep/cep \
  -H "Authorization: Bearer $TOKEN" \
  -H "DeviceToken: $DEVICE" \
  -H "Content-Type: application/json" \
  -d '{"cep": "01001000"}' | jq .
```

*Nota: Requer `jq` instalado para formatar o JSON (`apt install jq` ou `brew install jq`).*
