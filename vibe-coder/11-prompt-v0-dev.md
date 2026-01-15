# Prompt para V0.dev: Central de Comunicação (CRM de WhatsApp)

Prompt otimizado para gerar uma interface de chat profissional (estilo Intercom/Zendesk) pronta para conectar com a APIBrasil.

## Onde usar
**v0.dev** ou **Cursor Composer** (Modo React).

## Prompt para Copiar

```markdown
Atue como um Engenheiro de Frontend Senior e Designer de Produto.
Crie um Dashboard de "Central de Atendimento Multicanal".

Tecnologias:
- React (Next.js App Router)
- Shadcn/UI (Obrigatório para todos os componentes)
- Tailwind CSS (Estilização)
- Lucide React (Ícones)

Estrutura da Interface (Layout de 3 Colunas):

1.  **Sidebar de Navegação (Esquerda - 64px)**:
    -   Ícones para: Inbox, Contatos, Automações, Configurações.
    -   Avatar do usuário no rodapé.

2.  **Lista de Conversas (Centro-Esquerda - 300px)**:
    -   Busca no topo ("Buscar conversa...").
    -   Abas: "Abertos", "Fechados", "Bots".
    -   Item da lista: Avatar, Nome, Preview da mensagem (truncado), Horário, Badge de canal (WhatsApp/Instagram).

3.  **Janela de Chat Ativa (Centro - Flex)**:
    -   Header: Nome do Cliente, Status (Online/Offline), Botão "Finalizar Atendimento".
    -   Área de Mensagens: Balões estilo WhatsApp. Minhas mensagens à direita (Verde/Azul), Cliente à esquerda (Cinza). Suporte a texto, imagem e áudio.
    -   Input Area: Textarea auto-resize, clip para anexo, microfone para áudio, botão enviar.

4.  **Painel de Contexto (Direita - 300px - Collapsible)**:
    -   **Perfil do Cliente**: Foto, Nome, Telefone, Email.
    -   **Ações Rápidas (APIBrasil Integration)**:
        -   Botão "Enriquecer Dados": Ao clicar, simule um loading e mostre dados fictícios de CPF e Score.
        -   Botão "Consultar Veículo": Input de placa + Botão buscar.
    -   **Tags**: Badges (VIP, Novo, Reclamação).

Comportamento Mockado (Simulação):
-   Crie um estado local `messages` para simular o envio.
-   Ao enviar mensagem, adicione à lista localmente.
-   Simule um delay de 1s e adicione uma resposta automática "Recebemos sua mensagem!".

Estética:
-   Modo Dark Profissional (Slate/Zinc).
-   Bordas sutis, sombras suaves.
-   Tipografia Inter.
```
