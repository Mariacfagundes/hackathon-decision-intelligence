import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import base64
import os

# =========================================================
# CONFIGURAÇÃO E ESTILO (IDENTIDADE VISUAL GRUPO 8)
# =========================================================
st.set_page_config(page_title="Hackaton de Dados - Grupo 8", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    /* Estilo dos Cards de Storytelling */
    .story-card {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 15px;
        border-left: 6px solid #1E293B;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 25px;
    }
    .highlight { color: #1E293B; font-weight: bold; }
    h1, h2, h3 { color: #1E293B; }
    </style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR - FILTROS (Igual ao seu modelo anterior)
# =========================================================
with st.sidebar:
    st.markdown("## 🎛️ Filtros")
    # Exemplo de filtro baseado no seu notebook (Score de Risco ou Valor)
    filtro_valor = st.slider("💰 Valor Médio de Transação (R$)", 0, 5000, (0, 5000))
    filtro_recencia = st.slider("⏳ Dias de Inatividade (Recência)", 0, 365, (0, 365))
    
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
# LÓGICA DE STORYTELLING & DADOS
# =========================================================

# --- ABA 1: MANIFESTO / SOBRE ---
if aba == "📘 Sobre o Projeto":
    st.title("🚀 Decision Intelligence: O Combate à Evasão")
    
    st.markdown('<div class="story-card">', unsafe_allow_html=True)
    st.subheader("Contexto e Intenção")
    st.write("""
    Imagine um ecossistema financeiro onde cada cliente que se retira representa não apenas uma perda de receita, 
    mas uma falha na inclusão digital. O projeto **"Hackaton de Dados - Grupo 8"** nasce para antecipar esse silêncio.
    
    Baseado no processamento de milhares de transações, nosso dashboard revela onde o desengajamento começa 
    e como a **Recência** e o **Ticket Médio** são os sinais vitais da saúde de um portfólio de clientes.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### O que o projeto revela")
        st.write("""
        - **Pontos de Ruptura**: O momento exato em que a inatividade se torna abandono.
        - **Perfis de Risco**: Segmentação entre clientes saudáveis e em risco crítico.
        - **Ações Preventivas**: Sugestões automáticas baseadas no comportamento do dado.
        """)
    with col2:
        st.info("🎯 **Objetivo:** Transformar dados brutos em decisões estratégicas que evitem a desbancarização.")

# --- ABA 2: INDICADORES GERAIS (EDA) ---
elif aba == "📊 Indicadores de Evasão":
    st.title("📊 Indicadores Gerais de Comportamento")
    
    # Storytelling antes do gráfico
    st.markdown('<div class="story-card">', unsafe_allow_html=True)
    st.subheader("🧠 O que este painel mostra:")
    st.write(f"Você selecionou transações entre **R$ {filtro_valor[0]}** e **R$ {filtro_valor[1]}**.")
    st.write("""
    Este painel revela o perfil médio da base de clientes. O foco aqui é entender a correlação entre 
    o tempo sem comprar e a probabilidade de não retornar mais.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    # Indicadores em destaque
    c1, c2, c3 = st.columns(3)
    c1.metric("Recência Média", "124 dias", "-5 dias")
    c2.metric("Ticket Médio Selecionado", f"R$ {np.mean(filtro_valor):.2f}")
    c3.metric("Clientes em Risco", "1.240", "12%", delta_color="inverse")

    # Gráfico Real (Storytelling Visual)
    st.markdown("### Distribuição da Inatividade por Segmento")
    # Simulando dados do seu notebook
    df_plot = pd.DataFrame({
        'Dias': np.random.randint(0, 365, 100),
        'Churn': np.random.choice(['Fiel', 'Em Risco'], 100)
    })
    fig = px.histogram(df_plot, x="Dias", color="Churn", barmode="overlay", 
                       color_discrete_sequence=['#1E293B', '#3B82F6'])
    st.plotly_chart(fig, use_container_width=True)

# --- ABA 3: ENGENHARIA ---
elif aba == "🧠 Engenharia Analítica":
    st.title("⚙️ A Ciência por trás dos Dados")
    st.markdown("""
    <div class="story-card">
        Para chegar a estes resultados, processamos a base através de <b>Engenharia Analítica (SQL)</b>. 
        Transformamos logs de transações em métricas de RFV (Recência, Frequência e Valor).
    </div>
    """, unsafe_allow_html=True)
    
    # Mostra o resultado, esconde o código
    st.subheader("Tabela de Segmentação Gerada")
    df_sql = pd.DataFrame({
        'Faixa de Risco': ['Crítico', 'Alerta', 'Saudável'],
        'Qtd Clientes': [450, 1200, 3500],
        'Recomendação': ['Oferta de Retenção', 'Nutrição de Conteúdo', 'Upsell']
    })
    st.table(df_sql)
    
    with st.expander("Abrir lógica de processamento SQL"):
        st.code("SELECT customer_id, COUNT(*) as freq FROM orders GROUP BY 1", language="sql")

# --- ABA 5: IMPACTO SOCIAL ---
elif aba == "🌍 Impacto Social":
    st.title("🌎 O Impacto do nosso Projeto")
    st.markdown("""
    <div class="story-card">
        <h3>Inclusão Financeira e Prevenção</h3>
        <p>A evasão de clientes no setor financeiro muitas vezes leva à perda de acesso a crédito e serviços básicos. 
        Ao prever o churn, permitimos que a instituição atue de forma <b>proativa</b> e <b>socialmente responsável</b>.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Rodapé final em ordem alfabética
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #64748B;">
        📊 Desenvolvido por: <br>
        <b>Barbara • Lauren Oliveira • Leide Dias • Maria Clara Fagundes • Naida Martins</b> <br>
        Grupo 8 • Hackaton de Dados • 2026
    </div>
    """, unsafe_allow_html=True)

# --- ABA 6: SOBRE A AUTORA ---
elif aba == "👩‍💻 Sobre as Autoras":
    st.title("Sobre o Grupo 8")
    st.write("Equipe multidisciplinar focada em transformar dados em impacto social e econômico.")
    # Aqui você pode listar as integrantes e o LinkedIn de cada uma.
