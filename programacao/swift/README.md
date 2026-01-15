# Consumindo APIBrasil MCP com Swift

Exemplo nativo para iOS/macOS usando `URLSession` e `async/await`.

## 1. Código (APIService.swift)

```swift
import Foundation

struct ConsultaCEP: Codable {
    let cep: String
}

struct Endereco: Codable {
    let logradouro: String
    let bairro: String
    let localidade: String
    let uf: String
}

func consultarCEP(cep: String) async {
    let url = URL(string: "https://gateway.apibrasil.io/api/v2/cep/cep")!
    
    // Configuração segura (idealmente use Info.plist ou Keychain)
    let token = "SEU_BEARER_TOKEN"
    let device = "SEU_DEVICE_TOKEN"
    
    var request = URLRequest(url: url)
    request.httpMethod = "POST"
    request.setValue("Bearer \(token)", forHTTPHeaderField: "Authorization")
    request.setValue(device, forHTTPHeaderField: "DeviceToken")
    request.setValue("application/json", forHTTPHeaderField: "Content-Type")
    
    let body = ConsultaCEP(cep: cep)
    request.httpBody = try? JSONEncoder().encode(body)
    
    do {
        print("📱 Buscando dados...")
        let (data, response) = try await URLSession.shared.data(for: request)
        
        guard let httpResponse = response as? HTTPURLResponse, httpResponse.statusCode == 200 else {
            print("❌ Erro na API")
            return
        }
        
        if let jsonString = String(data: data, encoding: .utf8) {
            print("✅ Resposta: \(jsonString)")
        }
        
        // Decodificação (Opcional)
        // let endereco = try JSONDecoder().decode(Endereco.self, from: data)
        // print(endereco.logradouro)
        
    } catch {
        print("Erro de conexão: \(error.localizedDescription)")
    }
}

// Uso (em um contexto async)
Task {
    await consultarCEP(cep: "01001000")
}
```
