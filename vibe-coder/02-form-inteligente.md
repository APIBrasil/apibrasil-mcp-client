# Formulário Inteligente (CEP e CPF)

Este exemplo cria um formulário de cadastro de alta conversão que preenche o endereço automaticamente pelo CEP e valida o CPF em tempo real.

## Onde usar
Copie o prompt abaixo e cole no **v0.dev**, **Bolt.new** ou **Cursor Composer**.

## Prompt para Copiar

```markdown
Atue como um Especialista em React Hook Form e Zod.
Crie um componente de formulário de cadastro chamado `SmartSignupForm`.

Stack:
- React Hook Form (Gerenciamento de estado)
- Zod (Validação de schema)
- Shadcn/UI (Componentes visuais) ou Tailwind CSS puro
- Axios (API)

Campos:
1.  **Nome Completo**: Validação de mínimo 2 nomes.
2.  **CPF**: Use uma biblioteca de validação ou regex para garantir formato `000.000.000-00` e validade matemática.
3.  **CEP**: Máscara `00000-000`. Ao completar 8 dígitos, disparar busca automática.
4.  **Endereço** (Rua, Bairro, Cidade, UF): Inputs `readOnly` que são preenchidos pela API.
5.  **Número e Complemento**: Campos livres.

Lógica de Automação (CEP):
Use um `useEffect` ou o hook `watch` para monitorar o campo CEP.
Quando válido (8 dígitos):
1.  Mostre um spinner/skeleton nos campos de endereço.
2.  Faça GET/POST em `https://gateway.apibrasil.io/api/v2/cep/cep`.
    -   Payload: `{ "cep": "valor_limpo" }`
    -   Headers: Auth via `process.env.NEXT_PUBLIC_APIBRASIL_TOKEN`.
3.  Preencha os campos automaticamente com `setValue`.
4.  Foque o cursor no campo "Número".

Tratamento de Erros:
- Se o CEP não existir, exiba erro no campo e permita digitação manual.
- Se a API falhar, notifique o usuário suavemente.

Estética:
- Design minimalista, focado em conversão.
- Botão de submit com estado de `isSubmitting`.
```
