# Consumindo APIBrasil MCP com Java

Exemplo usando Java 11+ (HttpClient nativo). Como não há SDK oficial estável para Java ainda, fazemos a conexão SSE e POST manualmente seguindo o protocolo.

## 1. Código (McpClient.java)

```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.concurrent.CompletableFuture;

public class McpClient {

    private static final String SERVER_URL = "https://mcp.apibrasil.cloud/mcp";
    
    // Tokens (Configure aqui)
    private static final String BEARER = "SEU_BEARER";
    private static final String DEVICE_TOKEN = "SEU_DEVICE_TOKEN";

    public static void main(String[] args) {
        HttpClient client = HttpClient.newHttpClient();

        // 1. Iniciar conexão SSE (GET)
        // Na prática, você precisaria de uma lib robusta de SSE para ler o stream continuamente.
        // Aqui simulamos o handshake inicial para pegar o Session ID.
        
        System.out.println("Nota: Para produção, use uma biblioteca SSE como 'okhttp-sse' ou 'spring-webflux'.");
        System.out.println("Este exemplo mostra a lógica do protocolo.");

        // Passo lógico:
        // 1. GET /mcp -> Recebe evento 'endpoint' com uri para POST (incluindo sessionId)
        // 2. POST /mcp?sessionId=... -> Envia JSON-RPC {"method": "tools/call", ...}
        
        // Exemplo de Payload JSON-RPC para chamar a tool
        String jsonRpcPayload = "{"
                + "\"jsonrpc\": \"2.0\","
                + "\"method\": \"tools/call\","
                + "\"id\": 1,"
                + "\"params\": {"
                + "  \"name\": \"cep_lookup\","
                + "  \"arguments\": {"
                + "    \"cep\": \"01001000\","
                + "    \"bearer\": \"" + BEARER + "\","
                + "    \"deviceToken\": \"" + DEVICE_TOKEN + "\""
                + "  }"
                + "}"
                + "}";
                
        System.out.println("Payload a enviar (após obter SessionID): " + jsonRpcPayload);
    }
}
```

**Dica:** Para projetos Java sérios, recomendamos usar o **Spring AI**, que está integrando suporte a MCP nativamente.
