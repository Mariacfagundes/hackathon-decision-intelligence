import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    confusion_matrix
)

# =========================================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================================

st.set_page_config(
    page_title="Decision Intelligence Platform",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CSS PREMIUM
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background-color: #F8FAFC;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #111827 0%, #1E293B 100%);
}

h1 {
    color: #111827;
    font-size: 42px !important;
    font-weight: 700 !important;
}

h2, h3 {
    color: #1E293B;
    font-weight: 600;
}

p, label {
    color: #334155;
}

.card {
    background: white;
    padding: 28px;
    border-radius: 18px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.06);
    border: 1px solid #E2E8F0;
}

.hero {
    background: linear-gradient(135deg, #4F46E5, #7C3AED);
    padding: 50px;
    border-radius: 25px;
    color: white;
}

.hero h1 {
    color: white !important;
    font-size: 48px !important;
}

.hero p {
    color: #E0E7FF;
    font-size: 18px;
}

.insight {
    background: #EEF2FF;
    border-left: 8px solid #6366F1;
    padding: 22px;
    border-radius: 14px;
}

.footer {
    background: #111827;
    color: white;
    padding: 40px;
    border-radius: 20px;
    text-align: center;
}

.metric-box {
    background: white;
    padding: 25px;
    border-radius: 18px;
    text-align: center;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.06);
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# BASE SIMULADA
# =========================================================

np.random.seed(42)

n = 2000

clientes = pd.DataFrame({

    "cliente": range(1, n+1),

    "total_gasto": np.random.randint(100, 6000, n),

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

# =========================================================
# MACHINE LEARNING
# =========================================================

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

# =========================================================
# MENU
# =========================================================

pagina = st.sidebar.radio(
    "📌 Navegação",
    [
        "Home",
        "Análise Exploratória",
        "Inteligência SQL",
        "Estatística e Probabilidade",
        "Machine Learning",
        "Decision Intelligence",
        "Impacto Social"
    ]
)

# =========================================================
# HOME
# =========================================================

if pagina == "Home":

    st.markdown("""
    <div class="hero">

    <h1>📊 Decision Intelligence Platform</h1>

    <p>
    Sistema Inteligente de Análise de Perfil Financeiro e Consumo para
    Previsão de Evasão de Clientes e Geração de Recomendações Estratégicas.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Clientes",
        f"{len(clientes):,}".replace(",", ".")
    )

    col2.metric(
        "Receita",
        f"R$ {clientes['total_gasto'].sum():,.0f}".replace(",", ".")
    )

    col3.metric(
        "Taxa de Churn",
        f"{clientes['churn'].mean():.2%}"
    )

    col4.metric(
        "Ticket Médio",
        f"R$ {clientes['ticket_medio'].mean():,.2f}".replace(",", ".")
    )

    st.write("")
    st.write("")

    st.markdown("""
    ## 🎯 O Problema

    Empresas perdem milhares de clientes sem identificar os sinais
    comportamentais que antecedem o cancelamento.

    Isso impacta:
    - receita;
    - crescimento;
    - retenção;
    - sustentabilidade financeira.
    """)

    st.write("")

    st.markdown("""
    ## 🚀 A Solução

    Este projeto integra:
    - Python;
    - SQL;
    - Estatística;
    - Machine Learning;
    - Streamlit.

    para transformar dados em inteligência acionável.
    """)

    st.write("")

    st.markdown("""
    <div class="insight">

    <h3>💡 Insight Estratégico</h3>

    Clientes com baixa frequência de compra e maior tempo sem interação
    possuem risco significativamente maior de evasão.

    </div>
    """, unsafe_allow_html=True)

# =========================================================
# EDA
# =========================================================

elif pagina == "Análise Exploratória":

    st.title("📈 Análise Exploratória")

    fig1 = px.histogram(
        clientes,
        x="churn",
        color="churn",
        title="Distribuição de Churn"
    )

    st.plotly_chart(fig1, use_container_width=True)

    fig2 = px.box(
        clientes,
        x="churn",
        y="total_gasto",
        color="churn",
        title="Distribuição de Gasto por Grupo"
    )

    st.plotly_chart(fig2, use_container_width=True)

    fig3 = px.box(
        clientes,
        x="churn",
        y="frequencia_compra",
        color="churn",
        title="Frequência de Compra por Grupo"
    )

    st.plotly_chart(fig3, use_container_width=True)

    fig4 = px.scatter(
        clientes,
        x="total_gasto",
        y="dias_sem_compra",
        color="faixa_risco",
        title="Perfil Financeiro e Risco"
    )

    st.plotly_chart(fig4, use_container_width=True)

    st.success("""
    Clientes com menor recorrência e maior tempo sem compra
    apresentam risco elevado de churn.
    """)

# =========================================================
# SQL
# =========================================================

elif pagina == "Inteligência SQL":

    st.title("🧠 Inteligência SQL")

    st.markdown("""
    O SQL foi utilizado para:
    - segmentação estratégica;
    - análise de churn;
    - perfil financeiro;
    - frequência de compra;
    - ticket médio;
    - análises probabilísticas.
    """)

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

    st.info("""
    Clientes com maior frequência apresentam menor probabilidade de evasão.
    """)

# =========================================================
# ESTATÍSTICA
# =========================================================

elif pagina == "Estatística e Probabilidade":

    st.title("📊 Estatística e Probabilidade")

    stats = pd.DataFrame({

        "Métrica": ["Média", "Mediana", "Desvio Padrão"],

        "Total Gasto": [
            clientes["total_gasto"].mean(),
            clientes["total_gasto"].median(),
            clientes["total_gasto"].std()
        ],

        "Pedidos": [
            clientes["total_pedidos"].mean(),
            clientes["total_pedidos"].median(),
            clientes["total_pedidos"].std()
        ]

    })

    st.dataframe(stats)

    churn_baixa_freq = clientes[
        clientes["frequencia_compra"] < 0.05
    ]["churn"].mean()

    st.metric(
        "P(churn | baixa frequência)",
        f"{churn_baixa_freq:.2%}"
    )

    st.warning("""
    A probabilidade de churn aumenta significativamente
    em clientes com baixa frequência de compra.
    """)

# =========================================================
# ML
# =========================================================

elif pagina == "Machine Learning":

    st.title("🤖 Machine Learning")

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

    fig5 = px.imshow(
        matriz,
        text_auto=True,
        title="Matriz de Confusão"
    )

    st.plotly_chart(fig5, use_container_width=True)

    st.info("""
    O modelo consegue prever antecipadamente clientes
    com maior probabilidade de evasão.
    """)

# =========================================================
# DECISION INTELLIGENCE
# =========================================================

elif pagina == "Decision Intelligence":

    st.title("🧪 Simulador Estratégico")

    st.write("""
    Simule cenários de comportamento do cliente
    e visualize o risco de churn em tempo real.
    """)

    gasto = st.slider(
        "💰 Total Gasto",
        0,
        6000,
        1000
    )

    pedidos = st.slider(
        "🛒 Quantidade de Pedidos",
        1,
        20,
        5
    )

    dias = st.slider(
        "📅 Dias Sem Compra",
        0,
        365,
        60
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
        "Probabilidade de Churn",
        f"{prob:.2%}"
    )

    if prob >= 0.7:

        st.error("""
        Alto risco de evasão.

        Recomendação:
        ação imediata de retenção.
        """)

    elif prob >= 0.3:

        st.warning("""
        Médio risco.

        Recomendação:
        campanhas de relacionamento.
        """)

    else:

        st.success("""
        Cliente saudável.
        """)

# =========================================================
# IMPACTO SOCIAL
# =========================================================

elif pagina == "Impacto Social":

    st.title("🌍 Inclusão Financeira e Impacto Social")

    st.markdown("""
    Este projeto possui foco em impacto social e inclusão financeira.

    A análise inteligente de dados permite:
    - reduzir evasão;
    - apoiar retenção sustentável;
    - identificar vulnerabilidade financeira;
    - gerar estratégias mais inclusivas.

    O objetivo é transformar dados em decisões mais humanas.
    """)

# =========================================================
# RODAPÉ
# =========================================================

st.write("")
st.write("")

st.markdown("""
<div class="footer">

<h2>👩‍💻 Desenvolvedoras</h2>

Projeto desenvolvido para o Hackathon Decision Intelligence.

<br>

<h3>🤝 Parceiros</h3>

Elas+ Tech • Ada Tech • Artemisia • Caixa • Fundo Socioambiental

<br><br>

Python • SQL • Machine Learning • Streamlit • Plotly • Scikit-Learn

</div>
""", unsafe_allow_html=True)
