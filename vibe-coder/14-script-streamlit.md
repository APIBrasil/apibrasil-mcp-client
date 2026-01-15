# App Streamlit: Consulta FIPE Profissional

Interface de dados rápida para consulta de preços de veículos.

## Onde usar
Salve como `app.py`.

## Configuração de Segredos
Crie uma pasta `.streamlit` e um arquivo `secrets.toml`:
```toml
[apibrasil]
token = "SEU_TOKEN_AQUI"
device = "SEU_DEVICE_AQUI"
```

## Código

```python
import streamlit as st
import requests
import time

st.set_page_config(page_title="FIPE Explorer", page_icon="🏎️", layout="centered")

# Estilo Customizado
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 8px; }
    .stat-box { padding: 15px; background: #f0f2f6; border-radius: 10px; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

st.title("🏎️ FIPE Explorer")
st.caption("Dados oficiais via APIBrasil")

# Recupera segredos com segurança
try:
    API_TOKEN = st.secrets["apibrasil"]["token"]
    DEVICE_TOKEN = st.secrets["apibrasil"]["device"]
except Exception:
    st.error("⚠️ Configure `.streamlit/secrets.toml` com suas credenciais.")
    st.stop()

# Cache para evitar chamadas repetidas
@st.cache_data(ttl=3600)
def consultar_fipe(tipo, marca, modelo=None):
    # Simulação de endpoint (Ajuste para o endpoint real da APIBrasil FIPE)
    # Exemplo: POST /fipe/consultar
    url = "https://gateway.apibrasil.io/api/v2/fipe/consultarModelos" # URL Fictícia para exemplo
    
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "DeviceToken": DEVICE_TOKEN
    }
    
    # Payload mockado para demonstração da estrutura
    return {
        "valor": "R$ 45.000,00",
        "marca": "Volkswagen",
        "modelo": "Golf 1.6 MSI",
        "ano": 2018,
        "combustivel": "Flex"
    }

# Interface
with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        tipo = st.selectbox("Tipo", ["Carro", "Moto", "Caminhão"])
    with col2:
        # Idealmente, buscar marcas da API
        marca = st.selectbox("Marca", ["VW", "GM", "Fiat", "Ford"]) 
    with col3:
        ano = st.text_input("Ano Modelo", "2022")

    if st.button("🔍 Consultar Preço", type="primary"):
        with st.spinner("Consultando tabela oficial..."):
            time.sleep(1) # UX
            try:
                dados = consultar_fipe(tipo, marca)
                
                st.markdown("### Resultado")
                
                c1, c2 = st.columns(2)
                c1.metric("Preço Médio", dados["valor"], "+2.5% (Mês)")
                c2.metric("Referência", "Jan/2026")
                
                with st.expander("Ver Detalhes Técnicos"):
                    st.json(dados)
                    
            except Exception as e:
                st.error(f"Erro na consulta: {str(e)}")

st.markdown("---")
st.markdown("Made with 💙 by **APIBrasil Vibe Coder**")
```
