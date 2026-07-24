# APIBrasil MCP Server - Usage Examples

This document provides examples of how to use the APIBrasil MCP Server with Claude Desktop or other MCP clients.

## Example Queries

Once configured, you can ask Claude to use the APIBrasil tools with natural language:

### CPF Lookup
```
Can you look up the CPF 123.456.789-00?
```

### CNPJ Lookup
```
What information can you find for CNPJ 12.345.678/0001-90?
```

### Postal Code (CEP) Lookup
```
What is the address for CEP 01310-100?
```
```
Find the location of postal code 20040-020
```

### Vehicle Information
```
Look up vehicle information for plate ABC-1234
```
```
What can you tell me about the car with plate XYZ-9876?
```

### FIPE Price Table
```
What is the FIPE market price for vehicle with plate ABC-1234?
```

### Correios Package Tracking
```
Track my Correios package with code AA123456789BR
```
```
What's the status of postal delivery AA987654321BR?
```

### WhatsApp Messaging
```
Send a WhatsApp message saying "Hello, this is a test!" to number 5511999999999
```

### WhatsApp File Sending
```
Send the file at https://example.com/document.pdf via WhatsApp to 5511999999999 with caption "Here is your document"
```

## Integration with Other MCP Clients

The server implements the standard MCP protocol and can be used with any MCP-compatible client. Here's how to configure it:

### Using with MCP Inspector

For debugging and testing, you can use the [MCP Inspector](https://github.com/modelcontextprotocol/inspector):

```bash
npx @modelcontextprotocol/inspector node /path/to/dist/index.js
```

Then set your environment variables:
```bash
export APIBRASIL_BEARER_TOKEN=your_token
export APIBRASIL_DEVICE_TOKEN=your_device_token
```

### Using Programmatically

You can also use the server programmatically in your own Node.js applications:

```javascript
import { spawn } from 'child_process';

const server = spawn('node', ['/path/to/dist/index.js'], {
  env: {
    ...process.env,
    APIBRASIL_BEARER_TOKEN: 'your_token',
    APIBRASIL_DEVICE_TOKEN: 'your_device_token'
  },
  stdio: ['pipe', 'pipe', 'pipe']
});

// Communicate with the server using MCP protocol via stdin/stdout
```

## API Rate Limits

Please refer to your APIBrasil account for rate limits and usage quotas. The free tier typically has the following limits:

- WhatsApp: Limited messages per day
- CPF/CNPJ: Limited lookups per day
- Other services: Check your plan details at https://apigratis.com.br

## Support

If you encounter any issues or have questions:

1. Check the main [README.md](README.md) for configuration details
2. Join the WhatsApp support group: https://chat.whatsapp.com/KsxrUGIPWvUBYAjI1ogaGs
3. Join the Telegram group: https://t.me/apigratisoficial
4. Visit the documentation: https://apibrasil.com.br/documentacoes
5. Open an issue on GitHub: https://github.com/APIBrasil/apibrasil-mcp-client/issues

## Tips

- Always ensure your credentials are properly set in the environment variables
- Test with the MCP Inspector before integrating with Claude Desktop
- Keep your Bearer Token and Device Token secure and never commit them to version control
- Use the .env file for local development (already added to .gitignore)
