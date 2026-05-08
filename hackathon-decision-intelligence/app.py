import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import base64
import os

# =========================================================
# CONFIGURAÇÃO E ESTILO (ESTILO "LIVRO DIGITAL")
# =========================================================
st.set_page_config(page_title="Hackathon de Dados - Grupo 8", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .story-card {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 15px;
        border-left: 8px solid #1E293B;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.05);
        margin-bottom: 25px;
        line-height: 1.6;
    }
    .author-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #e2e8f0;
        margin-bottom: 10px;
        text-align: center;
    }
    .sponsor-logo {
        filter: grayscale(100%);
        opacity: 0.7;
        transition: 0.3s;
        margin: 20px;
    }
    .sponsor-logo:hover { filter: grayscale(0%); opacity: 1; }
    h1, h2 { color: #1E293B; }
    </style>
""", unsafe_allow_html=True)

# =========================================================
# 🎛️ SIDEBAR - FILTROS E NAVEGAÇÃO
# =========================================================
with st.sidebar:
    st.markdown("## 🎛️ Filtros")
    st.markdown("📍 **Segmentação de Risco**")
    risco_selecionado = st.multiselect("Status do Cliente", ["Crítico", "Alerta", "Saudável"], default=["Crítico", "Alerta", "Saudável"])
    
    st.markdown("---")
    st.markdown("💰 **Filtro de Investimento**")
    renda_min, renda_max = st.slider("Valor Transacionado (R$)", 0, 5000, (0, 5000))

    st.markdown("---")
    st.markdown("### Escolha uma aba")
    aba = st.radio("", [
        "📘 Sobre o Projeto",
        "📊 Indicadores de Evasão",
        "🧠 Engenharia Analítica",
        "🤖 Inteligência Preditiva",
        "🌍 Impacto Social",
        "👩‍💻 Sobre as Autoras"
    ])

# =========================================================
# 📘 ABA 1: MANIFESTO / SOBRE
# =========================================================
if aba == "📘 Sobre o Projeto":
    st.title("🚀 Decision Intelligence: O Combate à Evasão")
    
    st.markdown('<div class="story-card">', unsafe_allow_html=True)
    st.subheader("Hackathon de Dados: Contexto e Intenção")
    st.write("""
    Imagine o sistema financeiro em um cenário de alta volatilidade: a perda de engajamento do cliente não é apenas uma métrica de churn, 
    é uma barreira para a sustentabilidade do negócio e para a inclusão bancária.
    
    O projeto **"Hackathon de Dados - Grupo 8"** nasce como uma resposta estratégica a essa transformação. 
    Com base nos dados processados (Olist/Telco), o dashboard revela onde o desengajamento está mais avançado e onde a 
    **Recência** aponta para novas demandas de retenção.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### O que o projeto revela:
    - **Pontos Críticos**: Identificamos municípios e perfis onde a inatividade supera os 90 dias.
    - **Índice de Risco**: Uma métrica composta que sintetiza Valor, Frequência e Recência.
    - **Oportunidades de Retenção**: Onde o mercado ainda é fértil para campanhas de fidelização e crédito orientado.
    """)

# =========================================================
# 📊 ABA 2: EDA (STORYTELLING COM DADOS)
# =========================================================
elif aba == "📊 Indicadores de Evasão":
    st.title("🌎 O Impacto da Inatividade na Base de Dados")
    
    st.markdown('<div class="story-card">', unsafe_allow_html=True)
    st.subheader("📊 Indicadores Gerais")
    st.write(f"Você selecionou perfis com gasto entre **R$ {renda_min}** e **R$ {renda_max}**.")
    st.write("""
    Este painel revela o perfil médio da base de clientes selecionada. Ao cruzar a inatividade com o valor gasto, 
    conseguimos visualizar a "Zona de Silêncio" — o momento em que o cliente deixa de interagir com o ecossistema.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    c1.metric("Média de Recência", "124 dias", "Crítico")
    c2.metric("Ticket Médio", f"R$ {(renda_min+renda_max)/2:.2f}")
    c3.metric("Taxa de Churn Prevista", "89.4%")

    st.markdown("### Distribuição de Comportamento")
    # Gráfico simulado baseado no seu notebook
    df_eda = pd.DataFrame({'Dias': np.random.normal(150, 60, 200), 'Status': np.random.choice(['Em Risco', 'Ativo'], 200)})
    fig = px.histogram(df_eda, x="Dias", color="Status", barmode="overlay", color_discrete_sequence=['#1E293B', '#FF7A00'])
    st.plotly_chart(fig, use_container_width=True)

# =========================================================
# 👩‍💻 ABA 6: SOBRE AS AUTORAS & PATROCINADORES
# =========================================================
elif aba == "👩‍💻 Sobre as Autoras":
    st.title("👩‍💻 Sobre as Autoras")
    
    st.markdown('<div class="story-card">', unsafe_allow_html=True)
    st.write("""
    Este projeto foi desenvolvido como parte do desafio **Conexão Desenvolve - Gamificação 2026**. 
    O **Grupo 8** uniu competências em Engenharia de Dados, Análise Fiscal e Inteligência de Negócio 
    para criar uma solução real para o mercado.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    # Grid das Integrantes
    col_a, col_b, col_c = st.columns(3)
    
    equipe = [
        {"nome": "Barbara", "link": "https://linkedin.com/in/barbara"},
        {"nome": "Lauren Oliveira", "link": "https://linkedin.com/in/lauren"},
        {"nome": "Leide Dias", "link": "https://linkedin.com/in/leide"},
        {"nome": "Maria Clara Fagundes", "link": "https://linkedin.com/in/mariaclara"},
        {"nome": "Maida Martins", "link": "https://linkedin.com/in/maida"}
    ]

    for i, integrante in enumerate(equipe):
        with [col_a, col_b, col_c][i % 3]:
            st.markdown(f"""
            <div class="author-card">
                <h4 style="margin:0; color:#1E293B;">{integrante['nome']}</h4>
                <p style="font-size:14px; color:#64748B;">Salvador, Bahia</p>
                <a href="{integrante['link']}" target="_blank" style="text-decoration:none; color:#3B82F6;">🔗 LinkedIn</a>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🤝 Patrocinadores e Parceiros")
    
    # Simulação dos Logotipos (Substitua pelos links reais das imagens se houver)
    st.markdown("""
    <div style="text-align: center;">
        <span style="margin: 20px; font-weight: bold; color: #64748B;">Ada+tech</span>
        <span style="margin: 20px; font-weight: bold; color: #64748B;">Artemisia</span>
        <span style="margin: 20px; font-weight: bold; color: #1E293B;">CAIXA</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: center; font-size: 14px; color: #94A3B8;">
        📊 Desenvolvido pelo Grupo 8 • Conexão Desenvolve • 2026
    </div>
    """, unsafe_allow_html=True)
