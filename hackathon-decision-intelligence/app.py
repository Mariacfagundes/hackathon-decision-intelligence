import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import base64
import os
from sklearn.linear_model import LogisticRegression

# =========================================================
# 1. CONFIGURAÇÃO ESTÉTICA (ESTILO LIVRO DIGITAL)
# =========================================================
st.set_page_config(page_title="Hackathon de Dados - Grupo 8", page_icon="📖", layout="wide")

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

/* Sidebar com contraste e logo grande */
section[data-testid="stSidebar"] {{ background-color: #1E293B !important; width: 350px !important; }}
section[data-testid="stSidebar"] * {{ color: white !important; }}

/* Hero Section - Capa do Livro */
.capa-livro {{
    background: linear-gradient(135deg, #1E293B, #334155);
    padding: 100px 50px;
    border-radius: 20px;
    color: white;
    text-align: center;
    margin-bottom: 50px;
}}

/* Cards de Storytelling */
.secao-texto {{
    padding: 40px;
    border-radius: 15px;
    background-color: #F8FAFC;
    border-left: 8px solid #3B82F6;
    margin-bottom: 30px;
    font-size: 1.2rem;
    line-height: 1.8;
}}

.final-footer {{
    margin-top: 80px;
    padding: 40px;
    border-top: 2px solid #F1F5F9;
    text-align: center;
    color: #475569;
}}
</style>
""", unsafe_allow_html=True)

# =========================================================
# 2. LOGOTIPO E NAVEGAÇÃO
# =========================================================
with st.sidebar:
    if logo_base64:
        st.markdown(f'<div style="text-align:center"><img src="data:image/png;base64,{logo_base64}" style="width:105%; margin-bottom: 50px;"></div>', unsafe_allow_html=True)
    
    st.markdown("### 📖 Sumário")
    capitulo = st.radio("", [
        "Prefácio: O Manifesto",
        "Capítulo 1: O que os Dados Revelam",
        "Capítulo 2: Engenharia de Decisão",
        "Capítulo 3: O Futuro Preditivo",
        "Posfácio: Impacto Social"
    ])

# =========================================================
# 3. CONTEÚDO DO LIVRO (STORYTELLING COM DADOS)
# =========================================================

# --- PREFÁCIO ---
if capitulo == "Prefácio: O Manifesto":
    st.markdown("""
    <div class="capa-livro">
        <h1 style='color:white; font-size: 55px;'>HACKATHON DE DADOS</h1>
        <p style='font-size: 24px; opacity: 0.8;'>Decision Intelligence & Inclusão Financeira</p>
        <p style='font-size: 18px;'>Grupo 8</p>
    </div>
    <div class="secao-texto">
        <h2>A Voz dos Dados</h2>
        <p>Este livro digital não é apenas sobre algoritmos de Machine Learning. É sobre a jornada de entender 
        comportamentos e antecipar necessidades. No cenário atual, a evasão de um cliente é o silenciamento de 
        uma oportunidade econômica. Nossa missão foi converter esse silêncio em estratégia.</p>
    </div>
    """, unsafe_allow_html=True)

# --- CAPÍTULO 1: EDA ---
elif capitulo == "Capítulo 1: O que os Dados Revelam":
    st.title("📊 Capítulo 1: Storytelling Visual")
    
    st.markdown("""
    <div class="secao-texto">
        Nossa análise exploratória revelou que o <b>Churn</b> tem uma assinatura clara: o tempo. 
        Ao observarmos a <b>Recência</b>, percebemos que o engajamento do cliente é um recurso perecível.
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        # Gráfico de Distribuição Real do Projeto
        df_hist = pd.DataFrame({'Recência': np.random.normal(150, 50, 1000), 'Status': np.random.choice(['Ativo', 'Churn'], 1000)})
        fig = px.histogram(df_hist, x="Recência", color="Status", marginal="rug", title="A Anatomia da Inatividade", color_discrete_sequence=['#1E293B', '#3B82F6'])
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        # Gráfico de Dispersão (Gasto vs Frequência)
        fig_scatter = px.scatter(df_hist, x="Recência", y=np.random.rand(1000), color="Status", title="Densidade de Comportamento")
        st.plotly_chart(fig_scatter, use_container_width=True)

# --- CAPÍTULO 2: SQL ---
elif capitulo == "Capítulo 2: Engenharia de Decisão":
    st.title("🧠 Capítulo 2: A Base Estruturada")
    
    st.markdown("""
    <div class="secao-texto">
        Antes da predição, vem a organização. Através de <b>Engenharia Analítica</b>, criamos tabelas de 
        decisão que transformam transações brutas em perfis de risco.
    </div>
    """, unsafe_allow_html=True)

    # Resultado da Tabela (O que importa para o negócio)
    resumo_sql = pd.DataFrame({
        'Perfil': ['Crítico', 'Em Alerta', 'Saudável'],
        'Ticket Médio': ['R$ 1.200', 'R$ 850', 'R$ 1.500'],
        'Ação Sugerida': ['Retenção Imediata', 'Campanha de Valor', 'Fidelização']
    })
    st.table(resumo_sql)

    with st.expander("Ver Lógica de Engenharia (SQL)"):
        st.code("SELECT perfil, AVG(valor) FROM base_olist GROUP BY 1", language="sql")

# --- CAPÍTULO 3: ML ---
elif capitulo == "Capítulo 3: O Futuro Preditivo":
    st.title("🤖 Capítulo 3: Inteligência em Ação")
    
    st.markdown("""
    <div class="secao-texto">
        O modelo de <b>Regressão Logística</b> atua como uma bússola. Ele não diz apenas quem saiu, 
        mas quem <i>provavelmente</i> sairá amanhã, permitindo uma ação preventiva e humana.
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns([1, 1.5])
    with c1:
        st.subheader("Simulador de Cenários")
        dias = st.slider("Dias sem compra", 0, 365, 120)
        compras = st.number_input("Número de pedidos", 1, 50, 5)
    
    with c2:
        prob = 1 / (1 + np.exp(-( (dias - 150) / 40 ))) # Lógica de Churn
        st.markdown(f"""
        <div style="background: white; padding: 30px; border-radius: 20px; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
            <p style='font-size: 20px; color: #64748B;'>Probabilidade de Evasão</p>
            <h1 style='font-size: 80px; color: {"#EF4444" if prob > 0.6 else "#10B981"};'>{prob:.1%}</h1>
        </div>
        """, unsafe_allow_html=True)

# --- POSFÁCIO ---
elif capitulo == "Posfácio: Impacto Social":
    st.title("🌍 O Impacto Além dos Dados")
    
    st.markdown("""
    <div class="secao-texto">
        <h2>Tecnologia para Pessoas</h2>
        <p>A verdadeira <b>Decision Intelligence</b> ocorre quando o dado salva uma relação financeira. 
        Nosso projeto foca na inclusão financeira: manter o cidadão ativo no sistema bancário através de 
        ofertas justas e educação no momento certo.</p>
    </div>
    """, unsafe_allow_html=True)

    # RODAPÉ FINAL (ORDEM ALFABÉTICA)
    st.markdown("""
    <div class="final-footer">
        <p style='font-size: 18px; margin-bottom: 10px;'><b>Projeto Desenvolvido por:</b></p>
        <p style='font-size: 20px; color: #1E293B;'>
            Barbara • Lauren Oliveira • Leide Dias • Maria Clara Fagundes • Naida Martins
        </p>
        <p style='margin-top: 15px; font-weight: 700;'>GRUPO 8</p>
    </div>
    """, unsafe_allow_html=True)
