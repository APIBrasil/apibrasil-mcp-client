# App de Consulta Veicular (Sinesp/Detran)

Prompt para criar uma interface mobile moderna para consulta de placas, focada em utilidade e rapidez.

## Onde usar
Perfeito para **v0.dev** (React Native/Expo), **FlutterFlow** (via AI Gen) ou **Cursor Composer**.

## Prompt para Copiar

```markdown
Atue como um Especialista em Mobile UI/UX.
Crie uma tela de aplicativo para "Consulta de Veículos" com visual profissional e dark mode.

Componentes Chave:
1.  **Header**: Título "Consulte Fácil" e menu hambúrguer.
2.  **Hero Section**:
    -   Texto de chamada: "Descubra o histórico de qualquer veículo".
    -   **Input de Placa**: Estilize este input para parecer uma placa de carro real (Fundo cinza claro, borda superior azul, tipografia monoescaçada grande).
    -   Validação: Aceite formato antigo (AAA-1234) e Mercosul (AAA1A23). Auto-capitalize.
3.  **Botão de Ação**: "Buscar Agora" (Largo, gradiente azul/verde).
4.  **Resultados (Card Expansível)**:
    -   Inicialmente oculto. Ao carregar, mostre Skeleton Loader.
    -   **Dados Principais**: Modelo, Marca, Ano, Cor (em destaque).
    -   **Status Legal**: Badge VERMELHA se houver Roubo/Furto, VERDE se regular.
    -   **Detalhes**: Município, UF, Chassi (parcial).

Lógica de Integração (Instruções para o código):
-   Ao submeter, validar regex de placa.
-   Fazer POST para `https://gateway.apibrasil.io/api/v2/vehicles/consulta`.
    -   Body: `{ "placa": "PLACA_LIMPA", "tipo": "nacional" }`
    -   Auth: Use variáveis `EXPO_PUBLIC_API_TOKEN` e `EXPO_PUBLIC_DEVICE_TOKEN`.
-   Tratar erros 404 (Placa não encontrada) e 401 (Token inválido).

Estilo:
-   Inspiração: Apps de fintech (Nubank, Inter).
-   Use animações suaves de entrada nos cards de resultado.
```
