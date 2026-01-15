# Disparo em Massa Inteligente (Python)

Script Python para envio de mensagens em massa com foco em segurança (anti-ban), logs detalhados e retomada de falhas.

## Onde usar
Salve como `campaign_sender.py`.

## Requisitos
```bash
pip install pandas requests python-dotenv
```

## Código Otimizado

```python
import pandas as pd
import requests
import time
import random
import os
import logging
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env
load_dotenv()

# Configuração de Logs
logging.basicConfig(
    filename='campanha.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

CONFIG = {
    "api_url": "https://gateway.apibrasil.io/api/v2/whatsapp/sendText",
    "token": os.getenv("APIBRASIL_TOKEN"),
    "device_token": os.getenv("APIBRASIL_DEVICE_TOKEN"),
    "min_delay": 15, # Segundos
    "max_delay": 45
}

def enviar_mensagem(nome, telefone):
    # Personalização da mensagem (Spintax simples)
    saudacoes = ["Olá", "Oi", "Tudo bem"]
    msg_base = f"{random.choice(saudacoes)} {nome}, aproveite nossa oferta exclusiva!"
    
    payload = {
        "number": str(telefone),
        "text": msg_base
    }
    
    headers = {
        "Authorization": f"Bearer {CONFIG['token']}",
        "DeviceToken": CONFIG['device_token'],
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(CONFIG["api_url"], json=payload, headers=headers)
        if response.status_code == 200:
            logging.info(f"SUCESSO: {nome} ({telefone})")
            print(f"✅ Enviado: {nome}")
            return True
        else:
            logging.error(f"FALHA: {nome} - {response.text}")
            print(f"❌ Falha: {nome}")
            return False
    except Exception as e:
        logging.error(f"ERRO CRITICO: {nome} - {str(e)}")
        return False

def main():
    if not CONFIG['token']:
        print("⚠️ ERRO: Configure o APIBRASIL_TOKEN no arquivo .env")
        return

    try:
        # Lê CSV (colunas: nome, telefone, status)
        df = pd.read_csv('lista_contatos.csv')
        
        # Filtra apenas quem ainda não recebeu (opcional)
        if 'status' not in df.columns:
            df['status'] = 'pendente'
            
    except FileNotFoundError:
        print("Arquivo lista_contatos.csv não encontrado.")
        return

    print(f"🚀 Iniciando campanha para {len(df)} contatos...")
    
    for index, row in df.iterrows():
        if row.get('status') == 'enviado':
            continue
            
        sucesso = enviar_mensagem(row['nome'], row['telefone'])
        
        if sucesso:
            df.at[index, 'status'] = 'enviado'
            # Salva progresso a cada envio para não perder em caso de crash
            df.to_csv('lista_contatos.csv', index=False)
        
        # Delay Humano (Anti-Spam)
        tempo = random.randint(CONFIG['min_delay'], CONFIG['max_delay'])
        print(f"⏳ Aguardando {tempo}s...")
        time.sleep(tempo)

    print("🏁 Campanha finalizada.")

if __name__ == "__main__":
    main()
```
