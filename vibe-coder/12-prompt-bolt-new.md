# Prompt para Bolt.new: SaaS de KYC (Validação Cadastral)

Prompt para criar um SaaS completo de verificação de identidade usando a stack moderna do Bolt.

## Onde usar
**Bolt.new** (StackBlitz).

## Prompt para Copiar

```markdown
Crie uma aplicação Fullstack para um SaaS de Background Check (KYC).

Stack:
- Remix (Framework Fullstack)
- Tailwind CSS
- Prisma + SQLite (Banco de dados local para dev)

Funcionalidades:

1.  **Tela de Consulta (Dashboard)**:
    -   Input centralizado para CPF/CNPJ (com máscara automática).
    -   Botão "Investigar".

2.  **API Route (Backend)**:
    -   Crie uma rota `action` no Remix em `app/routes/dashboard.tsx`.
    -   Essa rota deve chamar a APIBrasil (`https://gateway.apibrasil.io/api/v2/dados/cpf/credits`).
    -   **IMPORTANTE**: Use `process.env.APIBRASIL_TOKEN` para autenticação. Não hardcode tokens.
    -   Se a API falhar, retorne erro amigável para o frontend.

3.  **Visualização do Relatório**:
    -   Exiba os dados retornados em um Grid organizado:
        -   Dados Pessoais (Nome, Mãe, Nasc).
        -   Localização (Endereços).
        -   Score/Financeiro (Se disponível).
    -   Botão "Exportar PDF" (Gere um PDF simples com os dados).

4.  **Histórico**:
    -   Salve cada consulta bem-sucedida no banco SQLite (Data, Documento Consultado, ID da Transação).
    -   Mostre uma tabela "Últimas Consultas" no rodapé.

Design:
-   Corporativo e Confiável (Tons de Azul Marinho e Branco).
-   Use componentes de feedback visual (Toasts, Spinners).
```
