# APIBrasil MCP Server

Model Context Protocol (MCP) server for [APIBrasil](https://apibrasil.com.br) - providing Brazilian data services including WhatsApp API, CPF/CNPJ lookup, postal code lookup, vehicle information, and postal tracking.

## Features

This MCP server provides access to the following APIBrasil services:

- 🔍 **CPF Lookup**: Query Brazilian individual taxpayer registry data
- 🏢 **CNPJ Lookup**: Query Brazilian company registry data  
- 📮 **CEP Lookup**: Get address information from postal codes
- 🚗 **Vehicle Data**: Look up vehicle information by license plate
- 💰 **FIPE Table**: Get vehicle market prices from FIPE table
- 📦 **Correios Tracking**: Track Brazilian postal service deliveries
- 💬 **WhatsApp**: Send text messages and files via WhatsApp

## Prerequisites

- Node.js 18 or higher
- APIBrasil account with Bearer Token and Device Token (get yours at [apigratis.com.br](https://apigratis.com.br))

## Installation

### From Source

1. Clone the repository:
```bash
git clone https://github.com/APIBrasil/apibrasil-mcp-client.git
cd apibrasil-mcp-client
```

2. Install dependencies:
```bash
npm install
```

3. Build the project:
```bash
npm run build
```

4. Set up your credentials:
```bash
cp .env.example .env
# Edit .env and add your APIBrasil credentials
```

## Configuration

### Environment Variables

Create a `.env` file with your APIBrasil credentials:

```env
APIBRASIL_BEARER_TOKEN=your_bearer_token_here
APIBRASIL_DEVICE_TOKEN=your_device_token_here
```

### Claude Desktop Configuration

Add this to your Claude Desktop configuration file:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "apibrasil": {
      "command": "node",
      "args": [
        "/absolute/path/to/apibrasil-mcp-client/dist/index.js"
      ],
      "env": {
        "APIBRASIL_BEARER_TOKEN": "your_bearer_token_here",
        "APIBRASIL_DEVICE_TOKEN": "your_device_token_here"
      }
    }
  }
}
```

Replace `/absolute/path/to/apibrasil-mcp-client` with the actual path to your installation.

## Available Tools

### `consulta_cpf`
Query Brazilian CPF (individual taxpayer registry) data.

**Parameters:**
- `cpf` (string): CPF number in format XXX.XXX.XXX-XX or digits only

**Example:**
```
Look up CPF 123.456.789-00
```

### `consulta_cnpj`
Query Brazilian CNPJ (company registry) data.

**Parameters:**
- `cnpj` (string): CNPJ number in format XX.XXX.XXX/XXXX-XX or digits only

**Example:**
```
Look up CNPJ 12.345.678/0001-90
```

### `consulta_cep`
Get address information from Brazilian postal code (CEP).

**Parameters:**
- `cep` (string): CEP in format XXXXX-XXX or digits only

**Example:**
```
What is the address for CEP 01310-100?
```

### `consulta_placa`
Get vehicle information by license plate.

**Parameters:**
- `placa` (string): License plate in format ABC-1234 or ABC1D23

**Example:**
```
Look up vehicle with plate ABC-1234
```

### `consulta_fipe`
Get vehicle market price from FIPE table by license plate.

**Parameters:**
- `placa` (string): License plate in format ABC-1234 or ABC1D23

**Example:**
```
What is the FIPE price for vehicle ABC-1234?
```

### `rastreio_correios`
Track Brazilian postal service (Correios) deliveries.

**Parameters:**
- `code` (string): Tracking code (e.g., AA123456789BR)

**Example:**
```
Track Correios package AA123456789BR
```

### `whatsapp_send_text`
Send text message via WhatsApp.

**Parameters:**
- `number` (string): WhatsApp number with country code (e.g., 5511999999999)
- `text` (string): Message text

**Example:**
```
Send WhatsApp message "Hello!" to 5511999999999
```

### `whatsapp_send_file`
Send file via WhatsApp.

**Parameters:**
- `number` (string): WhatsApp number with country code
- `path` (string): URL or file path
- `options` (object, optional): Additional options like caption

**Example:**
```
Send file from URL https://example.com/image.jpg to 5511999999999
```

## Development

### Build
```bash
npm run build
```

### Watch Mode
```bash
npm run watch
```

## Support

- WhatsApp Group: https://chat.whatsapp.com/KsxrUGIPWvUBYAjI1ogaGs
- Telegram Group: https://t.me/apigratisoficial
- Documentation: https://apibrasil.com.br/documentacoes

## Additional Documentation

- [Usage Examples](USAGE.md) - Detailed examples and integration guides
- [Contributing Guide](CONTRIBUTING.md) - Guidelines for contributing to the project

## License

MIT

## Credits

Developed by [APIBrasil](https://github.com/APIBrasil) using the [Model Context Protocol](https://modelcontextprotocol.io).
