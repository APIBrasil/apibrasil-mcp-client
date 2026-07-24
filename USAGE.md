# APIBrasil MCP — Usage Examples

How to use the APIBrasil tools once your MCP client is connected to
`https://mcp.apibrasil.cloud/mcp`. For connection setup, see the
[README](./README.en.md) and [`conceitos/credenciais/`](./conceitos/credenciais/).

## Example queries

Once configured, ask your assistant (Claude, Cursor, etc.) in natural language:

### CPF lookup
```
Can you look up the CPF 123.456.789-00?
```

### CNPJ lookup
```
What information can you find for CNPJ 12.345.678/0001-90?
```

### Postal code (CEP) lookup
```
What is the address for CEP 01310-100?
```
```
Find the location of postal code 20040-020
```

### Vehicle information
```
Look up vehicle information for plate ABC-1234
```

### FIPE price table
```
What is the FIPE market price for the vehicle with plate ABC-1234?
```

### Correios package tracking
```
Track my Correios package with code AA123456789BR
```

### WhatsApp messaging
```
Send a WhatsApp message saying "Hello, this is a test!" to number 5511999999999
```

### WhatsApp file sending
```
Send the file at https://example.com/document.pdf via WhatsApp to 5511999999999 with caption "Here is your document"
```

## Debugging with MCP Inspector

To inspect the available tools and try calls by hand, wrap the `mcp-remote`
bridge with the [MCP Inspector](https://github.com/modelcontextprotocol/inspector):

```bash
npx @modelcontextprotocol/inspector \
  npx mcp-remote https://mcp.apibrasil.cloud/mcp \
    --header "X-Apibrasil-Bearer:YOUR_BEARER_TOKEN" \
    --header "DeviceToken:YOUR_DEVICE_TOKEN"
```

## Programmatic usage

To call the endpoint from your own code, use the official MCP SDKs — see the
ready-to-run examples under [`programacao/`](./programacao/) (Node.js, Python,
Go, Java, C#, PHP, and more). They connect via **Streamable HTTP** and pass your
credentials as headers or tool arguments.

## Rate limits

Rate limits and quotas depend on your APIBrasil plan. Check your account and the
official documentation at [doc.apibrasil.io](https://doc.apibrasil.io).

## Support

1. Check the [README](./README.md) for configuration details.
2. Read [`conceitos/troubleshooting/`](./conceitos/troubleshooting/) for common errors (402/403/410/422).
3. Documentation: [doc.apibrasil.io](https://doc.apibrasil.io).
4. Open an issue: <https://github.com/APIBrasil/apibrasil-mcp-client/issues>.

## Tips

- Never commit your Bearer Token or Device Token — use `env`/secret managers and placeholders.
- Test with the MCP Inspector before wiring the endpoint into your client.
