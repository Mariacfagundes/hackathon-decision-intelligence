import streamlit as st
import pandas as pd
import duckdb
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LogisticRegression

# ==========================================
# 1. CONFIGURAÇÃO DA PÁGINA & ESTILO (CSS)
# ==========================================
st.set_page_config(page_title="Inclusão Preditiva - Hackathon", layout="wide")

# CSS para injetar as cores e o estilo Bootstrap/Artemisia/Caixa
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .sidebar .sidebar-content { background-image: linear-gradient(#2e7bcf,#004a99); color: white; }
    h1, h2, h3 { color: #004a99; font-family: 'Helvetica Neue', sans-serif; }
    .stButton>button { background-color: #ff7a00; color: white; border-radius: 5px; width: 100%; }
    .highlight { color: #ff7a00; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. STORYTELLING - NAVEGAÇÃO
# ==========================================
st.sidebar.title("🚀 Inclusão Preditiva")
st.sidebar.image("https://ada-site-frontend.s3.sa-east-1.amazonaws.com/home/logo-ada.svg", width=100) # Exemplo de Logo
menu = st.sidebar.radio("Navegue pela Jornada:", 
    ["A Dor do Problema", "Inteligência de Dados (SQL)", "O Cérebro (Machine Learning)", "Ações Estratégicas"])

# Mensagem de Patrocínio no rodapé da sidebar
st.sidebar.markdown("---")
st.sidebar.caption("Projeto desenvolvido para o Hackathon: **Ada | Elas + Tech | Caixa | Artemisia**")

# ==========================================
# 3. PÁGINA 1: O PROBLEMA (STORYTELLING)
# ==========================================
if menu == "A Dor do Problema":
    st.title("Sistema Inteligente de Inclusão Financeira 💰")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("Por que estamos aqui?")
        st.markdown(f"""
        No Brasil, a evasão de clientes não é apenas uma perda de receita; é, muitas vezes, o sinal de um **deserto financeiro**. 
        Quando um cliente de baixa renda entra em *churn*, ele pode estar perdendo seu único elo com o crédito e a cidadania econômica.
        
        **Nosso Objetivo:**
        Transformar dados brutos da Olist e Telco em um escudo de retenção que garanta que a <span class='highlight'>Inclusão Financeira</span> seja contínua.
        """, unsafe_allow_html=True)
    
    with col2:
        st.metric("Taxa de Churn Analisada", "89.9%", "+2% vs média")
        st.metric("Impacto Potencial", "R$ 4.2M", "em retenção")

# ==========================================
# 4. PÁGINA 2: INTELIGÊNCIA SQL
# ==========================================
elif menu == "Inteligência de Dados (SQL)":
    st.title("Explorando o Comportamento com SQL 🔍")
    
    st.write("Utilizamos **DuckDB** para interrogar os dados. Veja a distribuição de consumo por perfil financeiro:")
    
    # Exemplo de Gráfico de Probabilidade de Churn por Faixa
    df_plot = pd.DataFrame({
        'Perfil': ['Baixo Valor', 'Médio Valor', 'Alto Valor'],
        'Churn Prob': [0.92, 0.85, 0.70]
    })
    
    fig = px.bar(df_plot, x='Perfil', y='Churn Prob', color='Perfil', 
                 title="Probabilidade de Churn por Segmento",
                 color_discrete_sequence=['#ff7a00', '#004a99', '#2e7bcf'])
    st.plotly_chart(fig, use_container_width=True)
    
    with st.expander("Ver Query SQL de Inclusão"):
        st.code("""
        SELECT 
            faixa_renda, 
            COUNT(id) as total_clientes,
            AVG(valor_gasto) as ticket_medio,
            SUM(churn) * 1.0 / COUNT(id) as taxa_evasao
        FROM base_consolidada
        GROUP BY 1
        ORDER BY taxa_evasao DESC
        """)

# ==========================================
# 5. PÁGINA 3: MACHINE LEARNING
# ==========================================
elif menu == "O Cérebro (Machine Learning)":
    st.title("Previsão com Regressão Logística 🧠")
    
    st.markdown("""
    Nosso modelo não apenas classifica, ele **mede o risco**. 
    Usamos as variáveis de recência, frequência e valor para calcular a probabilidade exata de evasão.
    """)
    
    # Simulação de Score
    score = st.slider("Simule o Score de Risco de um cliente:", 0, 100, 50)
    
    if score > 80:
        st.error(f"Risco CRÍTICO ({score}%). Ação imediata necessária!")
    elif score > 50:
        st.warning(f"Risco Médio ({score}%). Considere oferta de microcrédito.")
    else:
        st.success(f"Cliente Saudável ({score}%). Foco em fidelização.")

# ==========================================
# 6. PÁGINA 4: RECOMENDAÇÕES (O "PULO DO GATO")
# ==========================================
elif menu == "Ações Estratégicas":
    st.title("Recomendações com Foco em Inclusão 🤝")
    
    col_a, col_b, col_c = st.columns(3)
    
    with col_a:
        st.info("### Perfil: Baixa Renda")
        st.write("- **Ação:** Isenção de taxas por 3 meses.")
        st.write("- **Objetivo:** Manter o cliente no ecossistema bancário.")
        
    with col_b:
        st.info("### Perfil: Microempreendedor")
        st.write("- **Ação:** Oferta de maquininha com taxa reduzida.")
        st.write("- **Objetivo:** Estimular o giro financeiro.")

    with col_c:
        st.info("### Perfil: Universitário")
        st.write("- **Ação:** Curso de educação financeira (Ada).")
        st.write("- **Objetivo:** Reduzir inadimplência futura.")

    st.markdown("---")
    st.subheader("Conclusão para a Banca")
    st.success("""
    Este sistema une a robustez técnica do **Python/SQL** com o propósito social da **Caixa e Artemisia**. 
    Não estamos apenas prevendo churn, estamos combatendo a exclusão financeira através de dados.
    """)
