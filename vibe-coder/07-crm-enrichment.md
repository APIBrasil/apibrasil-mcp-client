# Enriquecimento de Dados (CRM CLI)

Ferramenta de linha de comando (CLI) profissional para consultar e enriquecer dados de empresas (B2B) usando CNPJ.

## Onde usar
Salve como `crm-cli.js`.

## Setup
1.  Crie um arquivo `.env` com seus tokens.
2.  `npm install axios commander chalk dotenv`

## Código Otimizado

```javascript
#!/usr/bin/env node
require('dotenv').config();
const { Command } = require('commander');
const axios = require('axios');
const chalk = require('chalk');

const program = new Command();

const API_CONFIG = {
    token: process.env.APIBRASIL_TOKEN,
    device: process.env.APIBRASIL_DEVICE_TOKEN
};

if (!API_CONFIG.token) {
    console.error(chalk.red('❌ Erro: APIBRASIL_TOKEN não definido no .env'));
    process.exit(1);
}

program
  .version('2.0.0')
  .description('Enriquecimento de dados corporativos via APIBrasil');

program
  .command('enrich <cnpj>')
  .description('Busca dados detalhados de um CNPJ')
  .option('-j, --json', 'Output em formato JSON puro')
  .action(async (cnpj, options) => {
    // Remove caracteres não numéricos
    const cleanCnpj = cnpj.replace(/\D/g, '');
    
    if (!options.json) {
        console.log(chalk.blue(`🔍 Buscando dados para: ${cleanCnpj}...`));
    }

    try {
        const { data } = await axios.post(
            'https://gateway.apibrasil.io/api/v2/dados/cnpj/credits',
            { cnpj: cleanCnpj },
            { 
                headers: { 
                    'Authorization': `Bearer ${API_CONFIG.token}`,
                    'DeviceToken': API_CONFIG.device 
                } 
            }
        );

        if (options.json) {
            console.log(JSON.stringify(data, null, 2));
            return;
        }

        // Exibição Formatada (Human Readable)
        console.log(chalk.bold.green('\n✅ Empresa Encontrada:'));
        console.table({
            'Razão Social': data.razao_social,
            'Fantasia': data.nome_fantasia || '---',
            'Situação': data.situacao_cadastral,
            'Abertura': data.data_inicio_atividade,
            'Capital Social': data.capital_social
        });

        console.log(chalk.bold.yellow('\n📍 Localização:'));
        console.log(`${data.logradouro}, ${data.numero} ${data.complemento || ''}`);
        console.log(`${data.bairro} - ${data.municipio}/${data.uf}`);
        console.log(`CEP: ${data.cep}`);

    } catch (error) {
        const errMsg = error.response?.data?.message || error.message;
        console.error(chalk.red(`\n❌ Falha na consulta: ${errMsg}`));
    }
  });

program.parse(process.argv);
```
