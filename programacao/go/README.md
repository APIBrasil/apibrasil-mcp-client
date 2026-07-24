# Consumindo APIBrasil MCP com Go (Golang)

Exemplo básico usando `net/http`.

## 1. Código (main.go)

```go
package main

import (
	"bytes"
	"fmt"
	"io"
	"net/http"
)

// O servidor APIBrasil fala Streamable HTTP: mensagens JSON-RPC via POST em /mcp.
// O id da sessão volta no header "Mcp-Session-Id" da resposta do initialize.
const baseURL = "https://mcp.apibrasil.cloud/mcp"

func post(client *http.Client, body, sessionID string) (*http.Response, error) {
	req, _ := http.NewRequest("POST", baseURL, bytes.NewBufferString(body))
	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("Accept", "application/json, text/event-stream")
	if sessionID != "" {
		req.Header.Set("Mcp-Session-Id", sessionID)
	}
	return client.Do(req)
}

func main() {
	client := &http.Client{}

	// 1. initialize -> captura o Mcp-Session-Id
	initBody := `{"jsonrpc":"2.0","id":"init","method":"initialize","params":{"protocolVersion":"2025-06-18","clientInfo":{"name":"go","version":"1.0.0"},"capabilities":{}}}`
	initResp, err := post(client, initBody, "")
	if err != nil {
		panic(err)
	}
	sessionID := initResp.Header.Get("Mcp-Session-Id")
	initResp.Body.Close()
	fmt.Println("Sessão:", sessionID)

	// 2. notifications/initialized
	if n, err := post(client, `{"jsonrpc":"2.0","method":"notifications/initialized"}`, sessionID); err == nil {
		n.Body.Close()
	}

	// 3. tools/call -> cep_lookup
	callBody := `{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"cep_lookup","arguments":{"cep":"01001000","bearer":"SEU_BEARER","deviceToken":"SEU_DEVICE_TOKEN"}}}`
	callResp, err := post(client, callBody, sessionID)
	if err != nil {
		panic(err)
	}
	defer callResp.Body.Close()

	// A resposta pode vir como JSON puro ou stream SSE (linhas "data: {...}")
	out, _ := io.ReadAll(callResp.Body)
	fmt.Println(string(out))
}
```
