#!/usr/bin/env node
import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
  Tool,
} from '@modelcontextprotocol/sdk/types.js';
import axios, { AxiosInstance } from 'axios';

// APIBrasil Configuration
const APIBRASIL_BASE_URL = 'https://api.apibrasil.io/api';
const BEARER_TOKEN = process.env.APIBRASIL_BEARER_TOKEN || '';
const DEVICE_TOKEN = process.env.APIBRASIL_DEVICE_TOKEN || '';

interface APIBrasilConfig {
  bearerToken: string;
  deviceToken: string;
}

class APIBrasilClient {
  private client: AxiosInstance;
  private config: APIBrasilConfig;

  constructor(config: APIBrasilConfig) {
    this.config = config;
    this.client = axios.create({
      baseURL: APIBRASIL_BASE_URL,
      headers: {
        'Authorization': `Bearer ${config.bearerToken}`,
        'DeviceToken': config.deviceToken,
        'Content-Type': 'application/json',
      },
    });
  }

  // CPF Service - Lookup CPF data
  async consultaCPF(cpf: string): Promise<any> {
    const response = await this.client.post('/consulta-cpf', { cpf });
    return response.data;
  }

  // CNPJ Service - Lookup CNPJ data
  async consultaCNPJ(cnpj: string): Promise<any> {
    const response = await this.client.post('/consulta-cnpj', { cnpj });
    return response.data;
  }

  // CEP Service - Lookup postal code
  async consultaCEP(cep: string): Promise<any> {
    const response = await this.client.post('/cep', { cep });
    return response.data;
  }

  // Vehicles Service - Lookup vehicle by license plate
  async consultaPlaca(placa: string): Promise<any> {
    const response = await this.client.post('/vehicles/dados', { placa });
    return response.data;
  }

  // Vehicles FIPE Service - Get FIPE price table data
  async consultaFIPE(placa: string): Promise<any> {
    const response = await this.client.post('/vehicles/fipe', { placa });
    return response.data;
  }

  // Correios Service - Track postal delivery
  async rastreioCorreios(code: string): Promise<any> {
    const response = await this.client.post('/correios/rastreio', { code });
    return response.data;
  }

  // WhatsApp Service - Send text message
  async whatsappSendText(number: string, text: string): Promise<any> {
    const response = await this.client.post('/whatsapp/sendText', {
      number,
      text,
    });
    return response.data;
  }

  // WhatsApp Service - Send file
  async whatsappSendFile(number: string, path: string, options?: any): Promise<any> {
    const response = await this.client.post('/whatsapp/sendFile', {
      number,
      path,
      options,
    });
    return response.data;
  }
}

// Define available tools
const TOOLS: Tool[] = [
  {
    name: 'consulta_cpf',
    description: 'Consulta dados de CPF (Cadastro de Pessoas Físicas) brasileiro. Retorna informações detalhadas sobre um CPF.',
    inputSchema: {
      type: 'object',
      properties: {
        cpf: {
          type: 'string',
          description: 'CPF no formato XXX.XXX.XXX-XX ou apenas números',
        },
      },
      required: ['cpf'],
    },
  },
  {
    name: 'consulta_cnpj',
    description: 'Consulta dados de CNPJ (Cadastro Nacional de Pessoa Jurídica) brasileiro. Retorna informações da empresa.',
    inputSchema: {
      type: 'object',
      properties: {
        cnpj: {
          type: 'string',
          description: 'CNPJ no formato XX.XXX.XXX/XXXX-XX ou apenas números',
        },
      },
      required: ['cnpj'],
    },
  },
  {
    name: 'consulta_cep',
    description: 'Consulta informações de endereço através do CEP (Código de Endereçamento Postal) brasileiro.',
    inputSchema: {
      type: 'object',
      properties: {
        cep: {
          type: 'string',
          description: 'CEP no formato XXXXX-XXX ou apenas números',
        },
      },
      required: ['cep'],
    },
  },
  {
    name: 'consulta_placa',
    description: 'Consulta dados de veículo através da placa (Brasil). Retorna informações como marca, modelo, ano, etc.',
    inputSchema: {
      type: 'object',
      properties: {
        placa: {
          type: 'string',
          description: 'Placa do veículo no formato ABC-1234 ou ABC1D23',
        },
      },
      required: ['placa'],
    },
  },
  {
    name: 'consulta_fipe',
    description: 'Consulta tabela FIPE (preço de mercado) de veículo através da placa (Brasil).',
    inputSchema: {
      type: 'object',
      properties: {
        placa: {
          type: 'string',
          description: 'Placa do veículo no formato ABC-1234 ou ABC1D23',
        },
      },
      required: ['placa'],
    },
  },
  {
    name: 'rastreio_correios',
    description: 'Rastreia encomendas dos Correios do Brasil através do código de rastreamento.',
    inputSchema: {
      type: 'object',
      properties: {
        code: {
          type: 'string',
          description: 'Código de rastreamento dos Correios (ex: AA123456789BR)',
        },
      },
      required: ['code'],
    },
  },
  {
    name: 'whatsapp_send_text',
    description: 'Envia mensagem de texto via WhatsApp através da API do APIBrasil.',
    inputSchema: {
      type: 'object',
      properties: {
        number: {
          type: 'string',
          description: 'Número do WhatsApp com código do país (ex: 5511999999999)',
        },
        text: {
          type: 'string',
          description: 'Texto da mensagem a ser enviada',
        },
      },
      required: ['number', 'text'],
    },
  },
  {
    name: 'whatsapp_send_file',
    description: 'Envia arquivo via WhatsApp através da API do APIBrasil.',
    inputSchema: {
      type: 'object',
      properties: {
        number: {
          type: 'string',
          description: 'Número do WhatsApp com código do país (ex: 5511999999999)',
        },
        path: {
          type: 'string',
          description: 'URL ou caminho do arquivo a ser enviado',
        },
        options: {
          type: 'object',
          description: 'Opções adicionais (caption, etc)',
        },
      },
      required: ['number', 'path'],
    },
  },
];

// Create MCP Server
const server = new Server(
  {
    name: 'apibrasil-mcp-server',
    version: '1.0.0',
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// Initialize APIBrasil client
const apiClient = new APIBrasilClient({
  bearerToken: BEARER_TOKEN,
  deviceToken: DEVICE_TOKEN,
});

// Handle list_tools request
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return { tools: TOOLS };
});

// Handle call_tool request
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  try {
    switch (name) {
      case 'consulta_cpf': {
        const cpf = (args as any).cpf;
        const result = await apiClient.consultaCPF(cpf);
        return {
          content: [
            {
              type: 'text',
              text: JSON.stringify(result, null, 2),
            },
          ],
        };
      }

      case 'consulta_cnpj': {
        const cnpj = (args as any).cnpj;
        const result = await apiClient.consultaCNPJ(cnpj);
        return {
          content: [
            {
              type: 'text',
              text: JSON.stringify(result, null, 2),
            },
          ],
        };
      }

      case 'consulta_cep': {
        const cep = (args as any).cep;
        const result = await apiClient.consultaCEP(cep);
        return {
          content: [
            {
              type: 'text',
              text: JSON.stringify(result, null, 2),
            },
          ],
        };
      }

      case 'consulta_placa': {
        const placa = (args as any).placa;
        const result = await apiClient.consultaPlaca(placa);
        return {
          content: [
            {
              type: 'text',
              text: JSON.stringify(result, null, 2),
            },
          ],
        };
      }

      case 'consulta_fipe': {
        const placa = (args as any).placa;
        const result = await apiClient.consultaFIPE(placa);
        return {
          content: [
            {
              type: 'text',
              text: JSON.stringify(result, null, 2),
            },
          ],
        };
      }

      case 'rastreio_correios': {
        const code = (args as any).code;
        const result = await apiClient.rastreioCorreios(code);
        return {
          content: [
            {
              type: 'text',
              text: JSON.stringify(result, null, 2),
            },
          ],
        };
      }

      case 'whatsapp_send_text': {
        const { number, text } = args as any;
        const result = await apiClient.whatsappSendText(number, text);
        return {
          content: [
            {
              type: 'text',
              text: JSON.stringify(result, null, 2),
            },
          ],
        };
      }

      case 'whatsapp_send_file': {
        const { number, path, options } = args as any;
        const result = await apiClient.whatsappSendFile(number, path, options);
        return {
          content: [
            {
              type: 'text',
              text: JSON.stringify(result, null, 2),
            },
          ],
        };
      }

      default:
        throw new Error(`Unknown tool: ${name}`);
    }
  } catch (error: any) {
    return {
      content: [
        {
          type: 'text',
          text: `Error: ${error.message}\n${error.response?.data ? JSON.stringify(error.response.data, null, 2) : ''}`,
        },
      ],
      isError: true,
    };
  }
});

// Start the server
async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error('APIBrasil MCP Server running on stdio');
}

main().catch((error) => {
  console.error('Server error:', error);
  process.exit(1);
});
