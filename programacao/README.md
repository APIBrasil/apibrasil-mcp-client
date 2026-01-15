# Consumindo APIBrasil MCP com C# (.NET)

Exemplo usando `HttpClient`.

## 1. Código (Program.cs)

```csharp
using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using System.IO;

class Program
{
    static async Task Main(string[] args)
    {
        var client = new HttpClient();
        string baseUrl = "https://mcp.apibrasil.cloud/mcp";

        Console.WriteLine("Conectando ao SSE...");

        // 1. Ler stream SSE para capturar URL de sessão
        using (var stream = await client.GetStreamAsync(baseUrl))
        using (var reader = new StreamReader(stream))
        {
            string line;
            string postUrl = null;

            while ((line = await reader.ReadLineAsync()) != null)
            {
                Console.WriteLine($"Recebido: {line}");
                if (line.StartsWith("data: "))
                {
                    var endpoint = line.Substring(6).Trim();
                    // Constrói URL completa
                    postUrl = "https://mcp.apibrasil.cloud" + endpoint;
                    Console.WriteLine($"Session URL: {postUrl}");
                    break; // Sai do loop para fazer o POST
                }
            }
            
            // 2. Enviar comando (JSON-RPC) em outra thread/task ou conexão
            if (!string.IsNullOrEmpty(postUrl)) 
            {
                await CallTool(postUrl);
            }
        }
    }

    static async Task CallTool(string url)
    {
        var client = new HttpClient();
        
        string json = @"
        {
            ""jsonrpc"": ""2.0"",
            ""method"": ""tools/call"",
            ""id"": 1,
            ""params"": {
                ""name"": ""cep_lookup"",
                ""arguments"": {
                    ""cep"": ""01001000"",
                    ""bearer"": ""SEU_BEARER"",
                    ""deviceToken"": ""SEU_DEVICE_TOKEN""
                }
            }
        }";

        var content = new StringContent(json, Encoding.UTF8, "application/json");
        var response = await client.PostAsync(url, content);
        
        string result = await response.Content.ReadAsStringAsync();
        Console.WriteLine("\nResposta do Servidor:");
        Console.WriteLine(result);
    }
}
```
