# Consumindo APIBrasil MCP com Go (Golang)

Exemplo básico usando `net/http`.

## 1. Código (main.go)

```go
package main

import (
	"bufio"
	"bytes"
	"encoding/json"
	"fmt"
	"net/http"
	"strings"
)

const baseURL = "https://mcp.apibrasil.cloud/mcp"

func main() {
	fmt.Println("Conectando ao fluxo SSE...")

	// 1. Iniciar SSE para pegar SessionID
	resp, err := http.Get(baseURL)
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()

	scanner := bufio.NewScanner(resp.Body)
	var postURL string

	// Loop simples para ler o evento 'endpoint'
	// Em produção, use uma lib SSE completa
	for scanner.Scan() {
		line := scanner.Text()
		fmt.Println("Recebido:", line)

		if strings.HasPrefix(line, "data: ") {
			// O servidor manda o endpoint relativo no campo data
			endpoint := strings.TrimPrefix(line, "data: ")
			// Ajuste para montar URL completa
			if strings.HasPrefix(endpoint, "/") {
				// ex: /mcp?sessionId=xyz
				postURL = "https://mcp.apibrasil.cloud" + endpoint
			} else {
				postURL = endpoint
			}
			fmt.Println("Endpoint de POST detectado:", postURL)
			break // Temos o que precisamos para fazer chamadas
		}
	}

	if postURL == "" {
		fmt.Println("Não foi possível obter SessionID.")
		return
	}

	// 2. Fazer uma chamada de ferramenta (JSON-RPC)
	payload := map[string]interface{}{
		"jsonrpc": "2.0",
		"method":  "tools/call",
		"id":      1,
		"params": map[string]interface{}{
			"name": "cep_lookup",
			"arguments": map[string]interface{}{
				"cep":         "01001000",
				"bearer":      "SEU_BEARER",
				"deviceToken": "SEU_DEVICE_TOKEN",
			},
		},
	}

	jsonData, _ := json.Marshal(payload)
	postResp, err := http.Post(postURL, "application/json", bytes.NewBuffer(jsonData))
	if err != nil {
		panic(err)
	}
	defer postResp.Body.Close()

	fmt.Println("Chamada enviada. Status:", postResp.Status)
	// Ler resposta...
}
```
