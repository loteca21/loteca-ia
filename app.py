
import streamlit as st
import pandas as pd
import numpy as np
import requests
from datetime import datetime

st.set_page_config(layout="wide")
st.title("📊 Loteca IA - Prognósticos de Futebol Brasileiro")

st.markdown("### Jogos da Semana - Séries A, B e C")

@st.cache_data(ttl=86400)
def carregar_dados():
    # Exemplo simples com CSVs fictícios - na versão real, usaremos API ou scraping
    urls = {
        "Serie A": "https://example.com/brasileirao_serie_a.csv",
        "Serie B": "https://example.com/brasileirao_serie_b.csv",
        "Serie C": "https://example.com/brasileirao_serie_c.csv"
    }
    dados = {}
    for serie, url in urls.items():
        try:
            dados[serie] = pd.read_csv(url)
        except:
            dados[serie] = pd.DataFrame({"Time 1": [], "Time 2": [], "Data": [], "Rodada": []})
    return dados

# Simula dados para testes locais
def gerar_dados_teste():
    jogos = [
        {"Time 1": "Palmeiras", "Time 2": "Flamengo", "Rodada": 5},
        {"Time 1": "Vasco", "Time 2": "Grêmio", "Rodada": 5},
        {"Time 1": "Sport", "Time 2": "Ceará", "Rodada": 5},
        {"Time 1": "Paysandu", "Time 2": "Botafogo-SP", "Rodada": 5}
    ]
    return pd.DataFrame(jogos)

def gerar_prognostico(time1, time2):
    # Exemplo de lógica simples com random
    p = np.random.rand()
    if p < 0.4:
        return "Vitória do " + time1, "Time da casa tem histórico positivo."
    elif p < 0.7:
        return "Empate", "Equilíbrio entre os times baseado nos últimos jogos."
    else:
        return "Vitória do " + time2, f"{time2} vive melhor fase no campeonato."

abas = st.tabs(["Volante Loteca", "Consulta Manual", "Tabelas & Gráficos"])

with abas[0]:
    df = gerar_dados_teste()
    col1, col2 = st.columns(2)
    metade = len(df) // 2

    for idx, row in df.iterrows():
        with (col1 if idx <= metade else col2):
            st.markdown(f"**{row['Time 1']} x {row['Time 2']}**")
            resultado, motivo = gerar_prognostico(row['Time 1'], row['Time 2'])
            if st.button(f"🔍 Ver Análise - Jogo {idx+1}"):
                st.info(motivo)
            st.markdown(f"**Prognóstico:** {resultado}")

with abas[1]:
    st.subheader("Consulta Manual de Confronto")
    time_casa = st.text_input("Time da Casa")
    time_fora = st.text_input("Time Visitante")
    if st.button("Gerar Prognóstico Manual") and time_casa and time_fora:
        res, motivo = gerar_prognostico(time_casa, time_fora)
        st.success(f"Previsão para {time_casa} x {time_fora}: {res}")
        st.markdown(f"🧠 Motivo: {motivo}")

with abas[2]:
    st.subheader("🔢 Tabelas e Indicadores")
    st.markdown("Funcionalidade em desenvolvimento - em breve: classificação, desempenho e gráficos de gols.")
