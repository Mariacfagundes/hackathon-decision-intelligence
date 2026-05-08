import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configuração da Página
st.set_page_config(page_title="Grupo 8 - Decision Intelligence", layout="wide")

# Estilização Customizada (Inspirada no seu app de Economia Prateada)
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; border: 1px solid #e1e4e8; }
    .story-card { background-color: #ffffff; padding: 25px; border-radius: 15px; border-left: 5px solid #1E293B; margin-bottom: 20px; }
    h1, h2 { color: #1E293B; font-family: 'Helvetica'; }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR: O MENU DO CONHECIMENTO ---
with st.sidebar:
    st.image("logo.png", use_column_width=True) # Se tiver a logo na pasta
    st.title("Capítulos do Projeto")
    pagina = st.radio("Navegação", [
        "1. O Problema de Negócio",
        "2. Mergulho nos Dados (EDA)",
        "3. O Motor da Decisão (ML)",
        "4. Plano de Ação & Impacto"
    ])

# --- PÁGINA 1: O MANIFESTO ---
if pagina == "1. O Problema de Negócio":
    st.markdown('<div class="story-card">', unsafe_allow_html=True)
    st.title("🚀 O Desafio do Churn: Além dos Números")
    st.write("""
        No e-commerce moderno, reter um cliente é 5x mais barato do que adquirir um novo. 
        O **Grupo 8** debruçou-se sobre os dados da Olist para entender: 
        *Por que os nossos clientes param de comprar?* """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Clientes Analisados", "96.096")
    col2.metric("Taxa de Churn Atual", "89.94%", delta="-5%", delta_color="inverse")
    col3.metric("Ticket Médio", "R$ 144,86")

# --- PÁGINA 2: STORYTELLING COM DADOS (EDA) ---
elif pagina == "2. Mergulho nos Dados (EDA)":
    st.title("📊 Storytelling: O que os Dados nos Contam?")
    
    st.markdown("""
    <div class="story-card">
        <h3>A Recência é o nosso 'Sinal de Alerta'</h3>
        <p>Ao analisar a <b>Estatística Exploratória</b>, percebemos que o comportamento de churn não é aleatório. 
        Existe um 'ponto de não retorno' após 90 dias de inatividade.</p>
    </div>
    """, unsafe_allow_html=True)

    # Gráfico Real do seu Notebook: Churn por Perfil de Gasto
    # Dados extraídos da sua Query 1
    data_q1 = {
        'Perfil': ['Baixo Valor', 'Médio Valor', 'Alto Valor'],
        'Taxa de Churn': [100.0, 100.0, 100.0] # Conforme os dados do notebook
    }
    df_q1 = pd.DataFrame(data_q1)
    
    fig = px.bar(df_q1, x='Perfil', y='Taxa de Churn', 
                 title="Taxa de Churn por Perfil de Gasto",
                 color_discrete_sequence=['#3B82F6'])
    st.plotly_chart(fig, use_container_width=True)
    
    st.info("💡 **Insight de Negócio:** Surpreendentemente, clientes de 'Alto Valor' têm uma taxa de churn tão crítica quanto os de baixo valor, sugerindo que o preço não é o único fator de abandono.")

# --- PÁGINA 3: INTELIGÊNCIA PREDITIVA ---
elif pagina == "3. O Motor da Decisão (ML)":
    st.title("🤖 O Motor da Decisão")
    
    st.write("""
        Não queremos apenas reportar o passado, queremos prever o futuro. 
        Utilizamos um modelo de **Regressão Logística** para calcular a probabilidade de um cliente nos deixar.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Métricas do Modelo")
        st.write("- **Acurácia:** 100% (Base de teste)") # Conforme seu notebook
        st.write("- **F1-Score:** 1.00")
        
    with col2:
        st.markdown("### Simulador de Risco")
        input_gasto = st.number_input("Valor Gasto (R$)", 50, 5000, 150)
        input_recencia = st.slider("Dias sem comprar", 0, 365, 45)
        
        # Simulação simples da lógica do seu modelo
        risco = "Crítico" if input_recencia > 90 else "Baixo"
        st.subheader(f"Status do Cliente: {risco}")

# --- PÁGINA 4: IMPACTO E CONCLUSÃO ---
elif pagina == "4. Plano de Ação & Impacto":
    st.title("🎯 Estratégia de Retenção")
    
    st.markdown("""
    <div class="story-card">
        <h3>Recomendações Baseadas em Dados</h3>
        <ul>
            <li><b>Risco Crítico:</b> Oferta agressiva de cupom de recompra (Win-back).</li>
            <li><b>Risco Médio:</b> Campanha de nutrição via e-mail com lançamentos.</li>
            <li><b>Risco Baixo:</b> Programa de fidelidade para aumentar o LTV.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.success("Este projeto transforma dados brutos em decisões estratégicas para o crescimento sustentável.")

    # Rodapé com os nomes (Grupo 8)
    st.markdown("---")
    st.markdown("**Grupo 8:** Barbara • Lauren Oliveira • Leide Dias • Maria Clara Fagundes • Maida Martins")
