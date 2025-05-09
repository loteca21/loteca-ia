import streamlit as st

st.set_page_config(page_title="Loteca IA", layout="centered")
st.title("📋 Loteca IA - Prognósticos Semanais")

st.markdown("Visual inspirado no volante da Loteca, com palpites automáticos.")

jogos = [
    ("Flamengo x Palmeiras", "Empate", "Confronto equilibrado entre dois favoritos."),
    ("São Paulo x Vasco", "Vitória São Paulo", "São Paulo é forte como mandante, Vasco oscila."),
    ("Cruzeiro x Botafogo", "Vitória Botafogo", "Botafogo vive melhor momento na temporada."),
    ("Grêmio x Bahia", "Vitória Grêmio", "Grêmio costuma dominar em casa contra o Bahia."),
    ("Corinthians x Fortaleza", "Empate", "Times com rendimento semelhante recentemente."),
    ("Athletico x Santos", "Vitória Athletico", "Santos ainda se adapta à Série B, Athletico forte em casa."),
    ("Atlético-MG x Internacional", "Vitória Atlético-MG", "Internacional sofre fora de casa."),
]

for idx, (jogo, palpite, motivo) in enumerate(jogos, start=1):
    with st.expander(f"Jogo {idx}: {jogo}"):
        st.markdown(f"**Palpite:** `{palpite}`")
        st.markdown(f"**Justificativa:** {motivo}")
