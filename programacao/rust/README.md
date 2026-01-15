# Consumindo APIBrasil MCP com Rust

Exemplo usando **Tokio** (runtime assíncrono) e **Reqwest**.

## 1. Dependências (Cargo.toml)

```toml
[dependencies]
reqwest = { version = "0.11", features = ["json"] }
tokio = { version = "1", features = ["full"] }
serde = { version = "1.0", features = ["derive"] }
serde_json = "1.0"
```

## 2. Código (main.rs)

```rust
use reqwest::header;
use std::env;
use serde_json::json;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let token = env::var("APIBRASIL_TOKEN").unwrap_or("SEU_TOKEN".to_string());
    let device = env::var("APIBRASIL_DEVICE_TOKEN").unwrap_or("SEU_DEVICE".to_string());

    let mut headers = header::HeaderMap::new();
    headers.insert("Authorization", format!("Bearer {}", token).parse().unwrap());
    headers.insert("DeviceToken", device.parse().unwrap());
    headers.insert("Content-Type", "application/json".parse().unwrap());

    let client = reqwest::Client::builder()
        .default_headers(headers)
        .build()?;

    println!("🦀 Enviando requisição Rust...");

    let res = client.post("https://gateway.apibrasil.io/api/v2/cep/cep")
        .json(&json!({
            "cep": "01001000"
        }))
        .send()
        .await?;

    if res.status().is_success() {
        let body = res.text().await?;
        println!("✅ Sucesso: {}", body);
    } else {
        println!("❌ Erro: {:?}", res.status());
    }

    Ok(())
}
```
