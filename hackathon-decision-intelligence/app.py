import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix

# ==========================================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================================

st.set_page_config(
    page_title="Decision Intelligence",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# CSS PREMIUM
# ==========================================================

st.markdown("""
<style>

.main {
    background-color: #0F172A;
    color: white;
}

section[data-testid="stSidebar"] {
    background-color: #111827;
}

h1, h2, h3, h4 {
    color: #F8FAFC;
}

p, label, div {
    color: #E2E8F0;
}

.metric-card {
    background: linear-gradient(135deg, #1E293B, #111827);
    padding: 25px;
    border-radius: 18px;
    border: 1px solid #334155;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.25);
}

.storytelling {
    background: linear-gradient(135deg, #312E81, #1E1B4B);
    padding: 25px;
    border-radius: 18px;
    border-left: 8px solid #38BDF8;
    margin-bottom: 25px;
}

.footer {
    background-color: #111827;
    padding: 30px;
    border-radius: 20px;
    text-align: center;
    margin-top: 50px;
    border: 1px solid #334155;
}

.kpi {
    background-color: #1E293B;
    padding: 20px;
    border-radius: 16px;
    text-align: center;
    border: 1px solid #334155;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# TÍTULO
# ==========================================================

st.title("📊 Decision Intelligence Platform")

st.subheader(
    "Sistema Inteligente de Análise de Perfil Financeiro e Consumo para Previsão de Evasão de Clientes"
)

# ==========================================================
# STORYTELLING EXECUTIVO
# ==========================================================

st.markdown("""
<div class="storytelling">

## 🎯 Contexto Estratégico

O churn de clientes representa um dos maiores desafios para empresas orientadas a dados.

Este projeto utiliza:
- Python
- SQL
- Estatística
- Machine Learning
- Decision Intelligence

para prever risco de evasão, identificar padrões comportamentais e apoiar decisões estratégicas de retenção.

A solução transforma dados em inteligência acionável.

</div>
""", unsafe_allow_html=True)

# ==========================================================
# MENU
# ==========================================================

pagina = st.sidebar.radio(
    "📌 Navegação",
    [
        "Executive Overview",
        "Perfil Financeiro",
        "Inteligência SQL",
        "Machine Learning",
        "Decision Intelligence",
        "Inclusão Financeira"
    ]
)

# ==========================================================
# BASE SIMULADA
# ==========================================================

np.random.seed(42)

n = 1500

clientes = pd.DataFrame({

    "cliente": range(1, n+1),

    "total_gasto": np.random.randint(100, 5000, n),

    "total_pedidos": np.random.randint(1, 20, n),

    "dias_sem_compra": np.random.randint(1, 365, n)

})

clientes["ticket_medio"] = (
    clientes["total_gasto"] /
    clientes["total_pedidos"]
)

clientes["frequencia_compra"] = (
    clientes["total_pedidos"] /
    (clientes["dias_sem_compra"] + 1)
)

clientes["churn"] = np.where(
    clientes["dias_sem_compra"] > 120,
    1,
    0
)

# ==========================================================
# MACHINE LEARNING
# ==========================================================

X = clientes[[
    "total_gasto",
    "total_pedidos",
    "dias_sem_compra",
    "ticket_medio",
    "frequencia_compra"
]]

y = clientes["churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

modelo = LogisticRegression(max_iter=1000)

modelo.fit(X_train, y_train)

pred = modelo.predict(X_test)

accuracy = accuracy_score(y_test, pred)
precision = precision_score(y_test, pred)
recall = recall_score(y_test, pred)

clientes["score_risco"] = modelo.predict_proba(X)[:,1]

clientes["faixa_risco"] = pd.cut(
    clientes["score_risco"],
    bins=[0,0.3,0.7,1],
    labels=["Baixo","Médio","Alto"]
)

# ==========================================================
# RECOMENDAÇÕES
# ==========================================================

def recomendacao(score):

    if score >= 0.7:
        return "Oferecer benefício imediato"

    elif score >= 0.3:
        return "Campanha de retenção"

    else:
        return "Cliente saudável"

clientes["recomendacao"] = clientes["score_risco"].apply(recomendacao)

# ==========================================================
# PÁGINA 1
# ==========================================================

if pagina == "Executive Overview":

    st.header("📈 Executive Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Clientes",
        f"{len(clientes):,}".replace(",", ".")
    )

    col2.metric(
        "Taxa de Churn",
        f"{clientes['churn'].mean():.2%}"
    )

    col3.metric(
        "Receita Total",
        f"R$ {clientes['total_gasto'].sum():,.0f}".replace(",", ".")
    )

    col4.metric(
        "Ticket Médio",
        f"R$ {clientes['ticket_medio'].mean():,.2f}".replace(",", ".")
    )

    st.markdown("---")

    fig1 = px.histogram(
        clientes,
        x="churn",
        color="churn",
        title="Distribuição de Churn",
        color_discrete_sequence=["#38BDF8"]
    )

    st.plotly_chart(fig1, use_container_width=True)

    fig2 = px.box(
        clientes,
        x="churn",
        y="frequencia_compra",
        color="churn",
        title="Frequência de Compra por Grupo"
    )

    st.plotly_chart(fig2, use_container_width=True)

    st.success("""
    Insight Estratégico:
    
    Clientes com baixa frequência de compra e maior tempo sem interação apresentam risco significativamente maior de evasão.
    """)

# ==========================================================
# PÁGINA 2
# ==========================================================

elif pagina == "Perfil Financeiro":

    st.header("💳 Perfil Financeiro e Consumo")

    fig3 = px.scatter(
        clientes,
        x="total_gasto",
        y="dias_sem_compra",
        color="faixa_risco",
        size="ticket_medio",
        title="Perfil Financeiro e Risco de Churn"
    )

    st.plotly_chart(fig3, use_container_width=True)

    st.info("""
    Clientes com menor recorrência de compra possuem maior probabilidade de churn.
    
    O comportamento financeiro influencia diretamente o risco de evasão.
    """)

# ==========================================================
# PÁGINA 3
# ==========================================================

elif pagina == "Inteligência SQL":

    st.header("🧠 Inteligência SQL")

    st.code("""

WITH perfil AS (

SELECT
    customer_unique_id,
    total_gasto,
    total_pedidos,
    churn

FROM clientes

)

SELECT
    churn,
    AVG(total_gasto) AS gasto_medio,
    AVG(total_pedidos) AS pedidos_medio

FROM perfil

GROUP BY churn

""", language="sql")

    st.success("""
    O SQL foi utilizado para segmentações estratégicas, análise de churn e construção de indicadores executivos.
    """)

# ==========================================================
# PÁGINA 4
# ==========================================================

elif pagina == "Machine Learning":

    st.header("🤖 Machine Learning")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Accuracy",
        f"{accuracy:.2%}"
    )

    col2.metric(
        "Precision",
        f"{precision:.2%}"
    )

    col3.metric(
        "Recall",
        f"{recall:.2%}"
    )

    matriz = confusion_matrix(y_test, pred)

    fig4 = px.imshow(
        matriz,
        text_auto=True,
        title="Matriz de Confusão"
    )

    st.plotly_chart(fig4, use_container_width=True)

    st.info("""
    O modelo preditivo consegue identificar antecipadamente clientes com maior probabilidade de evasão.
    """)

# ==========================================================
# PÁGINA 5
# ==========================================================

elif pagina == "Decision Intelligence":

    st.header("🧪 Simulador Estratégico")

    st.write("""
    Altere os indicadores abaixo para simular cenários estratégicos de churn.
    """)

    gasto = st.slider(
        "💰 Total Gasto",
        0,
        5000,
        500
    )

    pedidos = st.slider(
        "🛒 Pedidos",
        1,
        20,
        3
    )

    dias = st.slider(
        "📅 Dias Sem Compra",
        0,
        365,
        90
    )

    novo_cliente = pd.DataFrame({

        "total_gasto": [gasto],
        "total_pedidos": [pedidos],
        "dias_sem_compra": [dias],
        "ticket_medio": [gasto/pedidos],
        "frequencia_compra": [pedidos/(dias+1)]

    })

    prob = modelo.predict_proba(novo_cliente)[0][1]

    st.metric(
        "📉 Probabilidade de Churn",
        f"{prob:.2%}"
    )

    if prob >= 0.7:

        st.error("""
        Cliente com ALTO risco de evasão.
        
        Recomendação:
        oferecer retenção imediata.
        """)

    elif prob >= 0.3:

        st.warning("""
        Cliente com MÉDIO risco.
        
        Recomendação:
        campanhas de relacionamento.
        """)

    else:

        st.success("""
        Cliente com BAIXO risco.
        
        Perfil saudável.
        """)

# ==========================================================
# PÁGINA 6
# ==========================================================

elif pagina == "Inclusão Financeira":

    st.header("🌍 Inclusão Financeira")

    st.markdown("""
    Este projeto também possui foco em impacto social.

    A análise preditiva permite:
    - identificar clientes vulneráveis;
    - reduzir evasão financeira;
    - apoiar retenção inteligente;
    - gerar estratégias mais inclusivas.

    A solução conecta tecnologia, dados e impacto social.
    """)

# ==========================================================
# RODAPÉ
# ==========================================================

st.markdown("""
<div class="footer">

<h3>👩‍💻 Desenvolvedoras</h3>

Projeto desenvolvido para o Hackathon Decision Intelligence.

<br>

<h3>🤝 Parceiros e Apoiadores</h3>

Elas+ Tech • Ada Tech • Artemisia • Caixa • Fundo Socioambiental

<br><br>

Tecnologias:
Python • SQL • Machine Learning • Streamlit • Scikit-Learn • Plotly

</div>
""", unsafe_allow_html=True)
