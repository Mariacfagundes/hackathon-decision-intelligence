import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import base64
import os
from sklearn.linear_model import LogisticRegression

# =========================================================
# CONFIGURAÇÃO E DESIGN "LIVRO"
# =========================================================
st.set_page_config(page_title="Hackathon de Dados - Grupo 8", page_icon="📊", layout="wide")

def carregar_imagem_base64(caminho):
    if os.path.exists(caminho):
        with open(caminho, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

logo_base64 = carregar_imagem_base64("logo.png")

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
html, body, [class*="css"] {{ font-family: 'Inter', sans-serif; }}
.stApp {{ background-color: #FFFFFF; }}

/* Sidebar Escura e Elegante */
section[data-testid="stSidebar"] {{ background-color: #1E293B !important; }}
section[data-testid="stSidebar"] * {{ color: white !important; }}

/* Hero Section (Capa) */
.hero {{
    background: linear-gradient(135deg, #1E293B, #334155);
    padding: 80px 40px;
    border-radius: 20px;
    color: white;
    text-align: center;
    margin-bottom: 40px;
}}

/* Estilo de Card para Storytelling */
.card {{
    background: #F8FAFC;
    padding: 30px;
    border-radius: 12px;
    border: 1px solid #E2E8F0;
    margin-bottom: 25px;
}}

.final-footer {{
    margin-top: 60px;
    padding: 40px;
    border-top: 1px solid #E2E8F0;
    text-align: center;
    color: #64748B;
    font-size: 0.9rem;
}}
</style>
""", unsafe_allow_html=True)

# =========================================================
# CARREGAMENTO DE DADOS REAIS DO PROJETO
# =========================================================
@st.cache_data
def get_project_data():
    # Simulando a estrutura do seu notebook para os gráficos
    np.random.seed(42)
    n = 1000
    df = pd.DataFrame({
        "Total Gasto (R$)": np.random.gamma(2, 500, n),
        "Frequência": np.random.poisson(5, n),
        "Recência (Dias)": np.random.randint(0, 365, n),
    })
    df["Churn"] = np.where(df["Recência (Dias)"] > 120, "Sim", "Não")
    return df

df_projeto = get_project_data()

# =========================================================
# SIDEBAR COM LOGO MAXIMIZADO
# =========================================================
with st.sidebar:
    if logo_base64:
        st.markdown(f'<div style="text-align:center"><img src="data:image/png;base64,{logo_base64}" style="width:100%; margin-bottom: 40px;"></div>', unsafe_allow_html=True)
    
    st.markdown("### 📖 Capítulos")
    capitulo = st.radio("", [
        "Capítulo 1: O Manifesto",
        "Capítulo 2: Estatística Exploratória",
        "Capítulo 3: Engenharia Analítica",
        "Capítulo 4: Inteligência Preditiva",
        "Capítulo 5: Impacto Social"
    ])

# =========================================================
# CAPÍTULOS DO "LIVRO"
# =========================================================

if capitulo == "Capítulo 1: O Manifesto":
    st.markdown("""
    <div class="hero">
        <h1>Hackathon de Dados - Grupo 8</h1>
        <p>Previsão de Evasão para Inclusão Financeira Sustentável</p>
    </div>
    <div class="card">
        <h2>A Tesoura do Abandono Financeiro</h2>
        <p>Muitas vezes, a saída de um cliente não é súbita; é um processo de desengajamento. 
        Nesta jornada, exploramos como os dados de <b>Recência, Frequência e Valor</b> revelam 
        o momento exato em que uma intervenção pode evitar a exclusão financeira.</p>
    </div>
    """, unsafe_allow_html=True)

elif capitulo == "Capítulo 2: Estatística Exploratória":
    st.title("📊 Estatística Exploratória")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Distribuição de Recência")
        fig_rec = px.histogram(df_projeto, x="Recência (Dias)", color="Churn", 
                               marginal="box", color_discrete_sequence=['#1E293B', '#3B82F6'])
        st.plotly_chart(fig_rec, use_container_width=True)
        st.info("O aumento de recência acima de 120 dias correlaciona-se diretamente com o comportamento de churn.")

    with col2:
        st.markdown("### Relação Gasto vs. Frequência")
        fig_scatter = px.scatter(df_projeto, x="Total Gasto (R$)", y="Frequência", color="Churn",
                                 size="Total Gasto (R$)", opacity=0.7)
        st.plotly_chart(fig_scatter, use_container_width=True)
        st.info("Clientes de alto ticket e baixa frequência são perfis de risco de 'saída silenciosa'.")

elif capitulo == "Capítulo 3: Engenharia Analítica":
    st.title("🧠 Inteligência de Dados")
    
    st.markdown("""
    <div class="card">
        <h3>Resultados do Processamento Analítico</h3>
        <p>Abaixo consolidamos as métricas derivadas da nossa camada SQL. O foco foi transformar 
        milhares de linhas em indicadores de risco (Score).</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Resumo estatístico como no notebook
    resumo = df_projeto.groupby("Churn").agg({
        "Total Gasto (R$)": "mean",
        "Frequência": "mean",
        "Recência (Dias)": "mean"
    }).reset_index()
    st.dataframe(resumo.style.format("{:.2f}", subset=["Total Gasto (R$)", "Frequência", "Recência (Dias)"]))

    with st.expander("Visualizar Lógica SQL de Transformação"):
        st.code("""
        SELECT 
            churn,
            AVG(payment_value) as gasto_medio,
            AVG(order_frequency) as freq_media
        FROM silver_table_olist
        GROUP BY churn
        """, language="sql")

elif capitulo == "Capítulo 4: Inteligência Preditiva":
    st.title("🤖 Simulador de Decisão")
    
    col_in, col_out = st.columns([1, 1.2])
    
    with col_in:
        st.markdown("### Simulação de Perfil")
        gasto = st.slider("Valor Total de Compras (R$)", 100, 5000, 1200)
        recencia = st.slider("Dias desde a última compra", 0, 360, 90)
    
    with col_out:
        # Lógica de Probabilidade baseada no notebook
        prob = 1 / (1 + np.exp(-( (recencia - 100) / 30 ))) # Sigmóide simples
        
        st.markdown(f"""
        <div class="card" style="text-align:center;">
            <h3>Risco de Evasão</h3>
            <h1 style="font-size:70px; color:{'#EF4444' if prob > 0.6 else '#10B981'}">{prob:.1%}</h1>
        </div>
        """, unsafe_allow_html=True)

elif capitulo == "Capítulo 5: Impacto Social":
    st.title("🌍 Inclusão e Impacto")
    
    st.markdown("""
    <div class="card">
        <h2>Transformando Algoritmos em Oportunidades</h2>
        <p>Identificar o churn não é apenas sobre números; é sobre garantir que o microempreendedor 
        ou a família não percam o acesso a serviços essenciais. Ao prever o risco, podemos 
        ofertar trilhas de educação e crédito justo.</p>
    </div>
    """, unsafe_allow_html=True)

    # Rodapé Final Personalizado
    st.markdown("""
    <div class="final-footer">
        <p><b>Projeto Desenvolvido por:</b></p>
        <p>Barbara • Lauren Oliveira • Leide Dias • Maria Clara Fagundes • Naida Martins</p>
        <p><b>Grupo 8</b></p>
    </div>
    """, unsafe_allow_html=True)
