# Dashboard de Vendas com Envio de WhatsApp

Este exemplo cria um painel administrativo. O objetivo é visualizar vendas e enviar comprovantes para clientes via WhatsApp com um clique.

## Onde usar
Copie o prompt abaixo e cole no **v0.dev**, **Bolt.new**, **Replit Agent** ou **Cursor Composer**.

## Prompt para Copiar

```markdown
Atue como um Desenvolvedor Frontend Senior especialista em React e UX.
Crie um Dashboard administrativo moderno para controle de vendas.

Stack Tecnológica:
- React (Vite ou Next.js)
- Tailwind CSS (Estilização)
- Lucide React (Ícones)
- Axios (Requisições HTTP)

Estrutura Visual:
1. **Sidebar Lateral**: Navegação (Dashboard, Pedidos, Clientes, Configurações).
2. **Área Principal**:
   - **Cabeçalho**: Título "Painel de Vendas" e User Avatar.
   - **KPIs Cards**: 3 cards no topo com ícones (Vendas Hoje, Ticket Médio, Total Enviado). Use cores suaves para diferenciar.
   - **Tabela de Pedidos**: Listagem com colunas ID, Cliente, Data, Valor (Formatado BRL), Status (Badge colorida) e Ações.

Funcionalidade Crítica (Botão WhatsApp):
Na coluna "Ações", adicione um botão com ícone do WhatsApp.
Ao clicar, execute a função `sendReceipt(order)`:
1.  Valide se o pedido tem telefone.
2.  Mude o estado do botão para `loading`.
3.  Faça um POST para `https://gateway.apibrasil.io/api/v2/whatsapp/sendText`.
    -   **Headers**:
        -   `Authorization`: `Bearer ${process.env.NEXT_PUBLIC_APIBRASIL_TOKEN}` (ou variável de ambiente equivalente)
        -   `DeviceToken`: `${process.env.NEXT_PUBLIC_APIBRASIL_DEVICE_TOKEN}`
    -   **Body**:
        ```json
        {
          "number": order.phone,
          "text": "Olá ${order.clientName}! Seu pedido #${order.id} no valor de ${order.value} foi confirmado. Obrigado!"
        }
        ```
4.  Exiba um `toast` de sucesso ou erro (use `sonner` ou similar).
5.  Retorne o botão ao estado normal.

Requisitos de Qualidade:
- Design Clean e Responsivo.
- Tratamento de erro (`try/catch`) na requisição.
- Não deixe tokens expostos no código, use variáveis de ambiente.
- Use mocks de dados para popular a tabela inicialmente.
```
