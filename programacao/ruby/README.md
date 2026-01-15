# Consumindo APIBrasil MCP com Ruby

Exemplo usando a biblioteca padrão `net/http`.

## 1. Código (client.rb)

```ruby
require 'uri'
require 'json'
require 'net/http'

TOKEN = ENV['APIBRASIL_TOKEN'] || 'SEU_TOKEN'
DEVICE = ENV['APIBRASIL_DEVICE_TOKEN'] || 'SEU_DEVICE'

url = URI("https://gateway.apibrasil.io/api/v2/cep/cep")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer #{TOKEN}"
request["DeviceToken"] = DEVICE
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "cep": "01001000"
})

begin
  puts "🔍 Buscando CEP..."
  response = http.request(request)
  
  if response.code == "200"
    data = JSON.parse(response.read_body)
    puts "✅ Resultado:"
    puts data
  else
    puts "❌ Erro: #{response.code}"
    puts response.read_body
  end
rescue StandardError => e
  puts "Erro de conexão: #{e.message}"
end
```

## Gem Recomendada
Para projetos maiores, recomenda-se usar a gem `faraday` ou `httpx` para uma interface mais fluida.
