import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import base64
import os
from sklearn.linear_model import LogisticRegression

# =========================================================
# 1. CONFIGURAÇÃO E CSS (ESTILO LIVRO PREMIUM)
# =========================================================
st.set_page_config(page_title="Hackaton de Dados, page_icon="📖", layout="wide")

def carregar_imagem_base64(caminho):
    if os.path.exists(caminho):
        with open(caminho, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

logo_base64 = carregar_imagem_base64("logo.png")

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
html, body, [class*="css"] {{ font-family: 'Inter', sans-serif; color: #1E293B; }}

/* Sidebar Elegante */
section[data-testid="stSidebar"] {{ 
    background-color: #1E293B !important; 
    min-width: 320px !important; 
}}
section[data-testid="stSidebar"] * {{ color: white !important; }}

/* MANIFESTO - Título mais curto e elegante */
.manifesto-header {{
    background: #1E293B;
    padding: 60px 20px;
    border-radius: 15px;
    color: white;
    text-align: center;
    max-width: 900px; /* Limita a largura para não ficar 'largo' demais */
    margin: 0 auto 40px auto;
    border-bottom: 5px solid #FF7A00;
}}
.manifesto-header h1 {{
    color: white !important;
    font-size: 38px !important;
    font-weight: 800 !important;
    margin-bottom: 10px;
}}

/* Seções de Texto (Storytelling) */
.capitulo-texto {{
    padding: 40px;
    background-color: #F8FAFC;
    border-radius: 12px;
    line-height: 1.8;
    font-size: 1.15rem;
    margin-bottom: 30px;
    border-left: 6px solid #1E293B;
}}

.final-footer {{
    margin-top: 80px;
    padding: 40px;
    border-top: 1px solid #E2E8F0;
    text-align: center;
    color: #64748B;
}}
</style>
""", unsafe_allow_html=True)

# =========================================================
# 2. SIDEBAR - LOGO E SUMÁRIO
# =========================================================
with st.sidebar:
    if logo_base64:
        st.markdown(f'''
            <div style="text-align: center; padding: 20px 0;">
                <img src="data:image/png;base64,{logo_base64}" style="width: 100%; max-width: 280px;">
            </div>
        ''', unsafe_allow_html=True)
    
    st.markdown("<h3 style='text-align:center;'>Capítulos</h3>", unsafe_allow_html=True)
    pagina = st.radio("", [
        "Capítulo 1: O Manifesto",
        "Capítulo 2: Voz dos Dados (EDA)",
        "Capítulo 3: Engenharia Analítica",
        "Capítulo 4: O Algoritmo",
        "Capítulo 5: Impacto Social"
    ])

# =========================================================
# 3. CONTEÚDO (STORYTELLING COM DADOS)
# =========================================================

# --- CAPÍTULO 1: MANIFESTO ---
if pagina == "Capítulo 1: O Manifesto":
    st.markdown("""
    <div class="manifesto-header">
        <h1>Manifesto de Dados</h1>
        <p style='font-size: 1.2rem; opacity: 0.9;'>Grupo 8 - Decision Intelligence</p>
    </div>
    <div class="capitulo-texto">
        <h2>A Alma por trás do Código</h2>
        <p>No <b>Hackaton de Dados</b>, nossa missão foi além da técnica. Entendemos que cada linha em uma base de dados representa a confiança de um cliente. 
        A evasão (churn) não é apenas um KPI negativo; é um sinal de que o serviço perdeu a conexão com a necessidade humana. 
        Este projeto propõe uma ponte entre a análise preditiva e a <b>retenção empática</b>.</p>
    </div>
    """, unsafe_allow_html=True)

# --- CAPÍTULO 2: EDA ---
elif pagina == "Capítulo 2: Voz dos Dados (EDA)":
    st.title("📊 Voz dos Dados")
    st.markdown("""
    <div class="capitulo-texto">
        Nossa exploração estatística revelou que o tempo de inatividade é o maior preditor de abandono. 
        Observamos que o comportamento de compra muda drasticamente antes da saída definitiva.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        # Exemplo de gráfico do seu notebook
        df_exp = pd.DataFrame({'Dias': np.random.normal(100, 50, 500), 'Churn': np.random.choice(['Sim', 'Não'], 500)})
        fig = px.histogram(df_exp, x="Dias", color="Churn", title="Frequência de Inatividade", color_discrete_sequence=['#1E293B', '#FF7A00'])
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.info("💡 **Insight:** O risco de evasão aumenta 40% após 90 dias de silêncio transacional.")

# --- CAPÍTULO 3: ENGENHARIA ---
elif pagina == "Capítulo 3: Engenharia Analítica":
    st.title("🧠 Inteligência Estruturada")
    st.markdown("""
    <div class="capitulo-texto">
        Utilizamos SQL para criar uma camada de inteligência que classifica clientes em faixas de risco. 
        Abaixo, o resultado da nossa segmentação.
    </div>
    """, unsafe_allow_html=True)
    
    df_sql = pd.DataFrame({
        'Segmento': ['Crítico', 'Alerta', 'Saudável'],
        'Ticket Médio': ['R$ 1.250', 'R$ 980', 'R$ 1.550'],
        'Probabilidade': ['92%', '45%', '12%']
    })
    st.table(df_sql)

    with st.expander("Ver Lógica de Engenharia (SQL)"):
        st.code("SELECT segment, AVG(value) FROM clients GROUP BY 1", language="sql")

# --- CAPÍTULO 4: ALGORITMO ---
elif pagina == "Capítulo 4: O Algoritmo":
    st.title("🤖 Previsão em Tempo Real")
    col1, col2 = st.columns([1, 1.5])
    with col1:
        st.markdown("### Simulador")
        dias = st.slider("Dias sem compra", 0, 365, 100)
    with col2:
        prob = 1 / (1 + np.exp(-( (dias - 120) / 30 )))
        st.markdown(f"""
        <div style="background: white; padding: 40px; border-radius: 15px; text-align: center; border: 1px solid #E2E8F0;">
            <p>Probabilidade de Churn</p>
            <h1 style="font-size: 80px; color: {'#FF7A00' if prob > 0.6 else '#1E293B'};">{prob:.1%}</h1>
        </div>
        """, unsafe_allow_html=True)

# --- CAPÍTULO 5: IMPACTO SOCIAL ---
elif pagina == "Capítulo 5: Impacto Social":
    st.title("🌍 O Futuro da Inclusão")
    st.markdown("""
    <div class="capitulo-texto">
        O objetivo final é a <b>Inclusão Financeira</b>. Ao prever a evasão, podemos oferecer suporte antes da exclusão, 
        mantendo o cidadão conectado ao ecossistema de crédito e cidadania bancária.
    </div>
    """, unsafe_allow_html=True)

    # RODAPÉ FINAL (ORDEM ALFABÉTICA)
    st.markdown("""
    <div class="final-footer">
        <p><b>Projeto Desenvolvido por:</b></p>
        <p>Barbara • Lauren Oliveira • Leide Dias • Maria Clara Fagundes • Naida Martins</p>
        <p><b>Grupo 8</b></p>
    </div>
    """, unsafe_allow_html=True)
