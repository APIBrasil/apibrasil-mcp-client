# Consumindo APIBrasil MCP com Java

Exemplo usando Java 11+ (HttpClient nativo). Como não há SDK oficial estável para Java ainda, falamos o protocolo Streamable HTTP manualmente (POST de mensagens JSON-RPC).

## 1. Código (McpClient.java)

```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class McpClient {

    private static final String SERVER_URL = "https://mcp.apibrasil.cloud/mcp";

    // Tokens (Configure aqui)
    private static final String BEARER = "SEU_BEARER";
    private static final String DEVICE_TOKEN = "SEU_DEVICE_TOKEN";

    // O servidor APIBrasil fala Streamable HTTP: mensagens JSON-RPC via POST em /mcp.
    // O id da sessão volta no header "Mcp-Session-Id" da resposta do initialize.
    static HttpResponse<String> post(HttpClient client, String body, String sessionId) throws Exception {
        HttpRequest.Builder b = HttpRequest.newBuilder(URI.create(SERVER_URL))
                .header("Content-Type", "application/json")
                .header("Accept", "application/json, text/event-stream")
                .POST(HttpRequest.BodyPublishers.ofString(body));
        if (sessionId != null) b.header("Mcp-Session-Id", sessionId);
        return client.send(b.build(), HttpResponse.BodyHandlers.ofString());
    }

    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();

        // 1. initialize -> captura o Mcp-Session-Id
        String initBody = "{\"jsonrpc\":\"2.0\",\"id\":\"init\",\"method\":\"initialize\",\"params\":{"
                + "\"protocolVersion\":\"2025-06-18\",\"clientInfo\":{\"name\":\"java\",\"version\":\"1.0.0\"},\"capabilities\":{}}}";
        HttpResponse<String> initResp = post(client, initBody, null);
        String sessionId = initResp.headers().firstValue("mcp-session-id").orElse(null);
        System.out.println("Sessão: " + sessionId);

        // 2. notifications/initialized
        post(client, "{\"jsonrpc\":\"2.0\",\"method\":\"notifications/initialized\"}", sessionId);

        // 3. tools/call -> cep_lookup
        String callBody = "{\"jsonrpc\":\"2.0\",\"id\":1,\"method\":\"tools/call\",\"params\":{"
                + "\"name\":\"cep_lookup\",\"arguments\":{"
                + "\"cep\":\"01001000\",\"bearer\":\"" + BEARER + "\",\"deviceToken\":\"" + DEVICE_TOKEN + "\"}}}";
        HttpResponse<String> callResp = post(client, callBody, sessionId);

        // A resposta pode vir como JSON puro ou como stream SSE (linhas "data: {...}")
        System.out.println(callResp.body());
    }
}
```

**Dica:** Para projetos Java sérios, recomendamos usar o **Spring AI**, que já integra suporte a MCP nativamente.
