# Contributing to APIBrasil MCP Server

Thank you for your interest in contributing to the APIBrasil MCP Server! This document provides guidelines for contributing to the project.

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally
3. Create a new branch for your feature or bugfix
4. Make your changes
5. Test your changes
6. Submit a pull request

## Development Setup

### Prerequisites

- Node.js 18 or higher
- npm or yarn
- Git
- APIBrasil account (for testing)

### Installation

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/apibrasil-mcp-client.git
cd apibrasil-mcp-client

# Install dependencies
npm install

# Set up environment variables
cp .env.example .env
# Edit .env with your credentials
```

### Building

```bash
# Build the project
npm run build

# Watch mode for development
npm run watch
```

## Project Structure

```
apibrasil-mcp-client/
├── src/
│   └── index.ts          # Main server implementation
├── dist/                 # Compiled JavaScript (generated)
├── .env.example          # Environment variables template
├── .gitignore           # Git ignore rules
├── LICENSE              # MIT License
├── README.md            # Main documentation
├── USAGE.md             # Usage examples
├── package.json         # Project dependencies
└── tsconfig.json        # TypeScript configuration
```

## Code Style

- Use TypeScript for all code
- Follow existing code formatting
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions focused and concise

## Adding New Features

### Adding a New APIBrasil Service Tool

To add a new tool for an APIBrasil service:

1. **Add the API method** to the `APIBrasilClient` class in `src/index.ts`:

```typescript
async newService(param: string): Promise<any> {
  const response = await this.client.post('/new-endpoint', { param });
  return response.data;
}
```

2. **Add the tool definition** to the `TOOLS` array:

```typescript
{
  name: 'new_service',
  description: 'Description of what this service does',
  inputSchema: {
    type: 'object',
    properties: {
      param: {
        type: 'string',
        description: 'Description of the parameter',
      },
    },
    required: ['param'],
  },
}
```

3. **Add the handler** in the `CallToolRequestSchema` handler:

```typescript
case 'new_service': {
  const param = (args as any).param;
  const result = await apiClient.newService(param);
  return {
    content: [
      {
        type: 'text',
        text: JSON.stringify(result, null, 2),
      },
    ],
  };
}
```

4. **Update documentation** in README.md and USAGE.md

5. **Test your changes** thoroughly

## Testing

Currently, the project uses manual testing. To test your changes:

1. Build the project: `npm run build`
2. Run the server: `node dist/index.js`
3. Test with MCP Inspector or Claude Desktop
4. Verify all tools work as expected

### Future Testing

We welcome contributions to add:
- Unit tests
- Integration tests
- Automated testing workflows

## Documentation

When adding new features or making changes:

1. Update the README.md if needed
2. Add usage examples to USAGE.md
3. Update inline code comments
4. Update TypeScript types and interfaces

## Submitting Changes

### Pull Request Process

1. **Update your branch** with the latest from main:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Ensure your code builds** without errors:
   ```bash
   npm run build
   ```

3. **Commit your changes** with clear messages:
   ```bash
   git commit -m "Add: New feature description"
   ```
   
   Use conventional commit prefixes:
   - `Add:` for new features
   - `Fix:` for bug fixes
   - `Update:` for updates to existing features
   - `Docs:` for documentation changes
   - `Refactor:` for code refactoring

4. **Push to your fork**:
   ```bash
   git push origin your-branch-name
   ```

5. **Create a Pull Request** on GitHub with:
   - Clear title describing the change
   - Detailed description of what was changed and why
   - Any related issue numbers
   - Screenshots or examples if applicable

### Pull Request Guidelines

- Keep changes focused and atomic
- One feature/fix per pull request
- Include relevant tests (when testing framework is added)
- Update documentation as needed
- Follow the existing code style
- Be responsive to feedback

## Reporting Bugs

When reporting bugs, please include:

1. **Description**: Clear description of the bug
2. **Steps to reproduce**: Detailed steps to reproduce the issue
3. **Expected behavior**: What you expected to happen
4. **Actual behavior**: What actually happened
5. **Environment**: 
   - Node.js version
   - Operating system
   - MCP client (Claude Desktop, Inspector, etc.)
6. **Logs**: Any relevant error messages or logs

## Feature Requests

We welcome feature requests! Please:

1. Check existing issues first to avoid duplicates
2. Clearly describe the feature and its use case
3. Explain why it would be beneficial
4. Provide examples if possible

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers and help them learn
- Focus on constructive feedback
- Respect differing viewpoints

## Questions?

- Join our WhatsApp group: https://chat.whatsapp.com/KsxrUGIPWvUBYAjI1ogaGs
- Join our Telegram group: https://t.me/apigratisoficial
- Open a GitHub issue for bugs or features
- Check the documentation: https://apibrasil.com.br/documentacoes

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

Thank you for contributing to APIBrasil MCP Server! 🚀
