# Consumindo APIBrasil MCP com C# (.NET)

Exemplo usando `HttpClient`.

## 1. Código (Program.cs)

```csharp
using System;
using System.Linq;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

class Program
{
    // O servidor APIBrasil fala Streamable HTTP: mensagens JSON-RPC via POST em /mcp.
    // O id da sessão volta no header "Mcp-Session-Id" da resposta do initialize.
    static readonly string ServerUrl = "https://mcp.apibrasil.cloud/mcp";

    static async Task Main()
    {
        using var client = new HttpClient();
        client.DefaultRequestHeaders.Add("Accept", "application/json, text/event-stream");

        // 1. initialize -> captura o Mcp-Session-Id
        string initBody = @"{""jsonrpc"":""2.0"",""id"":""init"",""method"":""initialize"",""params"":{""protocolVersion"":""2025-06-18"",""clientInfo"":{""name"":""csharp"",""version"":""1.0.0""},""capabilities"":{}}}";
        var initResp = await client.PostAsync(ServerUrl, new StringContent(initBody, Encoding.UTF8, "application/json"));
        string sessionId = initResp.Headers.TryGetValues("Mcp-Session-Id", out var values) ? values.First() : null;
        Console.WriteLine($"Sessão: {sessionId}");

        // 2. notifications/initialized
        await Send(client, @"{""jsonrpc"":""2.0"",""method"":""notifications/initialized""}", sessionId);

        // 3. tools/call -> cep_lookup
        string callBody = @"{""jsonrpc"":""2.0"",""id"":1,""method"":""tools/call"",""params"":{""name"":""cep_lookup"",""arguments"":{""cep"":""01001000"",""bearer"":""SEU_BEARER"",""deviceToken"":""SEU_DEVICE_TOKEN""}}}";
        var callResp = await Send(client, callBody, sessionId);

        // A resposta pode vir como JSON puro ou como stream SSE (linhas "data: {...}")
        Console.WriteLine("\nResposta do Servidor:");
        Console.WriteLine(await callResp.Content.ReadAsStringAsync());
    }

    static async Task<HttpResponseMessage> Send(HttpClient client, string body, string sessionId)
    {
        var req = new HttpRequestMessage(HttpMethod.Post, ServerUrl)
        {
            Content = new StringContent(body, Encoding.UTF8, "application/json")
        };
        if (!string.IsNullOrEmpty(sessionId)) req.Headers.Add("Mcp-Session-Id", sessionId);
        return await client.SendAsync(req);
    }
}
```
