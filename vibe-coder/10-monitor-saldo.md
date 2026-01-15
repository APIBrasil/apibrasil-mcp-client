# Monitor de Saldo (Dashboard Pessoal)

Uma ferramenta visual simples (HTML/JS) para verificar seu saldo e créditos na APIBrasil.

> **⚠️ AVISO DE SEGURANÇA:** Este arquivo é para uso **local** (no seu computador). Nunca hospede este arquivo em um servidor público, pois o Token é inserido no navegador.

## Onde usar
Salve como `dashboard.html` e abra com duplo clique.

## Código

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard APIBrasil</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
</head>
<body class="bg-slate-900 text-slate-200 min-h-screen flex items-center justify-center p-4">

    <div class="bg-slate-800 p-8 rounded-xl shadow-2xl w-full max-w-md border border-slate-700">
        <div class="flex items-center justify-center mb-6">
            <div class="bg-blue-600 p-3 rounded-full">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
            </div>
        </div>

        <h1 class="text-2xl font-bold text-center mb-2">Carteira APIBrasil</h1>
        <p class="text-slate-400 text-center text-sm mb-6">Consulte seus créditos em tempo real</p>
        
        <div class="space-y-4">
            <div>
                <label class="block text-xs font-bold uppercase tracking-wide text-slate-500 mb-1">Seu Token</label>
                <input type="password" id="token" 
                    class="w-full bg-slate-900 border border-slate-600 rounded px-4 py-3 text-white focus:outline-none focus:border-blue-500 transition" 
                    placeholder="Cole seu Bearer Token aqui">
            </div>

            <button onclick="checkBalance()" id="btn" 
                class="w-full bg-blue-600 hover:bg-blue-500 text-white font-bold py-3 px-4 rounded transition flex justify-center items-center">
                <span>Verificar Saldo</span>
            </button>
        </div>

        <!-- Card de Resultado -->
        <div id="result" class="mt-8 hidden bg-slate-900 rounded-lg p-6 text-center border border-slate-700 animate-fade-in">
            <span class="text-slate-400 text-sm">Saldo Disponível</span>
            <div id="balanceValue" class="text-4xl font-extrabold text-green-400 mt-2">R$ --,--</div>
            <div id="statusBadge" class="inline-block mt-3 px-3 py-1 rounded-full text-xs font-bold bg-green-900 text-green-300">
                ATIVO
            </div>
        </div>
        
        <p id="error" class="mt-4 text-red-400 text-center text-sm hidden"></p>
    </div>

    <script>
        async function checkBalance() {
            const token = document.getElementById('token').value.trim();
            const btn = document.getElementById('btn');
            const result = document.getElementById('result');
            const error = document.getElementById('error');
            const balanceEl = document.getElementById('balanceValue');

            if (!token) return alert('Token é obrigatório!');

            // UI Loading
            btn.disabled = true;
            btn.innerHTML = '<svg class="animate-spin h-5 w-5 mr-3" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg> Buscando...';
            result.classList.add('hidden');
            error.classList.add('hidden');

            try {
                // Mock da chamada (Ajuste para a URL real se necessário)
                const { data } = await axios.post('https://gateway.apibrasil.io/api/v2/balance', {}, {
                    headers: { 'Authorization': `Bearer ${token}` }
                });

                // Tratamento flexível do retorno
                const saldo = data.balance || data.saldo || data.credits || 0;
                
                balanceEl.innerText = new Intl.NumberFormat('pt-BR', { 
                    style: 'currency', currency: 'BRL' 
                }).format(saldo);

                result.classList.remove('hidden');
            } catch (err) {
                error.innerText = err.response?.data?.message || 'Falha ao consultar. Verifique seu token.';
                error.classList.remove('hidden');
            } finally {
                btn.disabled = false;
                btn.innerHTML = 'Verificar Saldo';
            }
        }
    </script>
</body>
</html>
```
