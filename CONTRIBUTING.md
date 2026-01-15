# Guia de Contribuição

Obrigado por considerar contribuir com o **APIBrasil MCP Client**! 🎉

Este repositório é uma base de conhecimento comunitária para centralizar configurações e exemplos de integração da APIBrasil com o ecossistema de IA.

## Como Contribuir

### 1. Adicionando uma Nova Integração

Se você testou a APIBrasil em uma nova ferramenta (IDE, Chatbot, Low-Code), siga estes passos:

1.  **Escolha a Categoria**:
    *   `clientes-ai/` (Frontends de Chat como Claude, LibreChat)
    *   `ide-editores/` (VS Code, JetBrains, Cursor)
    *   `chatbots-ai/` (Builders como Typebot, Flowise)
    *   `lowcode-automacao/` (n8n, Make, Zapier)
    *   `programacao/` (Exemplos de código puro)

2.  **Crie a Pasta**:
    Use o nome da ferramenta em *snake_case* (ex: `minha_ferramenta`).
    ```bash
    mkdir ide-editores/minha_ferramenta
    ```

3.  **Adicione a Documentação**:
    Crie um arquivo `README.md` dentro da pasta. Use este template básico:
    ```markdown
    # Integração com [Nome da Ferramenta]

    Breve descrição da ferramenta.

    ## Configuração
    Passo a passo...

    ## Exemplo
    Código ou screenshot...
    ```

4.  **Adicione Arquivos de Configuração (Opcional)**:
    Se a ferramenta usa arquivos JSON/YAML de configuração, inclua um exemplo na mesma pasta (ex: `settings.json`).

### 2. Atualizando o Índice

Sempre que adicionar ou remover pastas, você **deve** rodar o script de atualização para manter o `README.md` principal sincronizado:

```bash
python scripts/update_readme_tree.py
```

Se você não rodar este script, o CI (Integração Contínua) falhará e seu Pull Request não será aceito.

### 3. Padrão de JSON

Se estiver adicionando arquivos `.json`:
*   Certifique-se de que é um JSON válido.
*   Não deixe vírgulas sobrando no final de listas/objetos.
*   Use indentação de 2 ou 4 espaços.

## Reportando Bugs

Use a aba [Issues](https://github.com/apibrasil/apibrasil-mcp-client/issues) para reportar:
*   Configurações que pararam de funcionar.
*   Erros na documentação.
*   Sugestões de novas ferramentas.

---
**Dica:** Mantenha os exemplos simples e focados na conexão. Não inclua tokens reais nos seus commits!
