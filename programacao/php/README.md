# Consumindo APIBrasil MCP com PHP

Exemplo usando **Guzzle**, o cliente HTTP mais popular do ecossistema PHP (padrão no Laravel).

## 1. Instalação

```bash
composer require guzzlehttp/guzzle
```

## 2. Código (client.php)

```php
<?php

require 'vendor/autoload.php';

use GuzzleHttp\Client;
use GuzzleHttp\Exception\RequestException;

$token = getenv('APIBRASIL_TOKEN') ?: 'SEU_TOKEN_AQUI';
$device = getenv('APIBRASIL_DEVICE_TOKEN') ?: 'SEU_DEVICE_TOKEN';

$client = new Client([
    'base_uri' => 'https://gateway.apibrasil.io/api/v2/',
    'timeout'  => 10.0,
    'headers'  => [
        'Authorization' => 'Bearer ' . $token,
        'DeviceToken'   => $device,
        'Content-Type'  => 'application/json',
        'Accept'        => 'application/json'
    ]
]);

try {
    echo "🔍 Consultando CEP...\n";
    
    $response = $client->post('cep/cep', [
        'json' => [
            'cep' => '01001000'
        ]
    ]);

    $data = json_decode($response->getBody(), true);
    
    echo "✅ Endereço Encontrado:\n";
    print_r($data);

} catch (RequestException $e) {
    echo "❌ Erro na requisição:\n";
    if ($e->hasResponse()) {
        echo $e->getResponse()->getBody();
    } else {
        echo $e->getMessage();
    }
}
```

## Nota sobre MCP (SSE)
O PHP tradicional é síncrono (request-response). Para usar o protocolo MCP completo (que exige conexão SSE persistente), você precisaria de um loop de eventos assíncrono (como ReactPHP ou Swoole). Para aplicações web padrão (Laravel/Symfony), use a API REST conforme o exemplo acima.
