# app.py — Dashboard Streamlit Hackathon

```python
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# ======================================================
# CONFIGURAÇÃO DA PÁGINA
# ======================================================

st.set_page_config(
    page_title="Decision Intelligence",
    page_icon="📊",
    layout="wide"
)

# ======================================================
# CORES DO PROJETO
# Inspiradas em Ada Tech + Artemisia + Caixa
# ======================================================

COR_PRIMARIA = "#7B2CBF"
COR_SECUNDARIA = "#00B4D8"
COR_SUCESSO = "#2DC653"
COR_ALERTA = "#D62828"
FUNDO = "#F8F9FA"

# ======================================================
# CSS PERSONALIZADO
# ======================================================

st.markdown(f"""
<style>
.main {{
    background-color: {FUNDO};
}}

h1, h2, h3 {{
    color: {COR_PRIMARIA};
}}

.stMetric {{
    background-color: white;
    padding: 15px;
    border-radius: 15px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.08);
}}

.bloco-storytelling {{
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    border-left: 8px solid {COR_PRIMARIA};
    margin-bottom: 20px;
}}
</style>
""", unsafe_allow_html=True)

# ======================================================
# TÍTULO
# ======================================================

st.title("📊 Decision Intelligence")

st.subheader(
    "Sistema Inteligente de Análise de Perfil Financeiro e Consumo para Previsão de Evasão de Clientes"
)

st.markdown("---")

# ======================================================
# STORYTELLING
# ======================================================

st.markdown(f"""
<div class="bloco-storytelling">
<h3>🎯 Contexto do Problema</h3>

Empresas perdem milhares de clientes todos os anos sem compreender os principais sinais de evasão.

Este projeto utiliza:
<ul>
<li>Python</li>
<li>SQL</li>
<li>Machine Learning</li>
<li>Estatística</li>
<li>Decision Intelligence</li>
</ul>

para transformar dados em decisões estratégicas inteligentes.
</div>
""", unsafe_allow_html=True)

# ======================================================
# MENU LATERAL
# ======================================================

pagina = st.sidebar.radio(
    "📌 Navegação",
    [
        "Visão Geral",
        "Predição de Churn",
        "Simulador Estratégico"
    ]
)

# ======================================================
# BASE SIMULADA
# ======================================================

np.random.seed(42)

n = 1000

clientes = pd.DataFrame({
    "cliente": range(1, n+1),
    "total_gasto": np.random.randint(50, 5000, n),
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

# ======================================================
# MODELO ML
# ======================================================

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

clientes["score_risco"] = modelo.predict_proba(X)[:,1]

clientes["faixa_risco"] = pd.cut(
    clientes["score_risco"],
    bins=[0,0.3,0.7,1],
    labels=["Baixo","Médio","Alto"]
)

# ======================================================
# RECOMENDAÇÕES
# ======================================================

def recomendacao(score):
    if score >= 0.7:
        return "Oferecer benefício imediato"
    elif score >= 0.3:
        return "Campanha de retenção"
    else:
        return "Cliente saudável"

clientes["recomendacao"] = clientes["score_risco"].apply(recomendacao)

# ======================================================
# PÁGINA 1 — VISÃO GERAL
# ======================================================

if pagina == "Visão Geral":

    st.header("📈 Visão Geral Estratégica")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Clientes",
        f"{len(clientes):,}"
    )

    col2.metric(
        "Taxa de Churn",
        f"{clientes['churn'].mean():.2%}"
    )

    col3.metric(
        "Receita Total",
        f"R$ {clientes['total_gasto'].sum():,.0f}"
    )

    col4.metric(
        "Ticket Médio",
        f"R$ {clientes['ticket_medio'].mean():.2f}"
    )

    st.markdown("---")

    # GRÁFICO CHURN

    fig1 = px.histogram(
        clientes,
        x="churn",
        color="churn",
        title="Distribuição de Churn"
    )

    st.plotly_chart(fig1, use_container_width=True)

    # GRÁFICO FREQUÊNCIA

    fig2 = px.box(
        clientes,
        x="churn",
        y="frequencia_compra",
        color="churn",
        title="Frequência de Compra por Grupo"
    )

    st.plotly_chart(fig2, use_container_width=True)

    # GRÁFICO GASTO

    fig3 = px.scatter(
        clientes,
        x="total_gasto",
        y="dias_sem_compra",
        color="faixa_risco",
        title="Perfil Financeiro e Risco"
    )

    st.plotly_chart(fig3, use_container_width=True)

    st.markdown(f"""
    <div class="bloco-storytelling">
    <h3>📌 Insight Estratégico</h3>

    Clientes com maior tempo sem compra e menor frequência apresentam risco significativamente maior de churn.

    O modelo permite identificar esses sinais antecipadamente e apoiar ações inteligentes de retenção.
    </div>
    """, unsafe_allow_html=True)

# ======================================================
# PÁGINA 2 — PREDIÇÃO
# ======================================================

elif pagina == "Predição de Churn":

    st.header("🤖 Predição Inteligente de Churn")

    filtro = st.selectbox(
        "Filtrar Risco",
        ["Todos", "Alto", "Médio", "Baixo"]
    )

    tabela = clientes.copy()

    if filtro != "Todos":
        tabela = tabela[
            tabela["faixa_risco"] == filtro
        ]

    st.dataframe(
        tabela[[
            "cliente",
            "score_risco",
            "faixa_risco",
            "recomendacao"
        ]]
    )

    st.metric(
        "Accuracy do Modelo",
        f"{accuracy:.2%}"
    )

    st.markdown(f"""
    <div class="bloco-storytelling">
    <h3>🧠 Decision Intelligence</h3>

    O sistema identifica clientes com maior probabilidade de evasão e sugere ações estratégicas personalizadas.
    
    Isso permite decisões preventivas orientadas por dados.
    </div>
    """, unsafe_allow_html=True)

# ======================================================
# PÁGINA 3 — SIMULADOR
# ======================================================

elif pagina == "Simulador Estratégico":

    st.header("🧪 Simulador Estratégico de Churn")

    st.write(
        "Altere os indicadores do cliente e observe como o risco muda em tempo real."
    )

    gasto = st.slider(
        "💰 Total Gasto",
        0,
        5000,
        500
    )

    pedidos = st.slider(
        "🛒 Quantidade de Pedidos",
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
        st.error("⚠️ Cliente com ALTO risco de evasão")

    elif prob >= 0.3:
        st.warning("⚠️ Cliente com MÉDIO risco")

    else:
        st.success("✅ Cliente com BAIXO risco")

    st.markdown(f"""
    <div class="bloco-storytelling">
    <h3>🚀 Simulação Estratégica</h3>

    Esta funcionalidade permite testar cenários e apoiar decisões estratégicas em tempo real.

    O painel transforma dados em ações inteligentes de retenção.
    </div>
    """, unsafe_allow_html=True)

# ======================================================
# RODAPÉ
# ======================================================

st.markdown("---")

st.markdown(
    """
    ### 👩‍💻 Desenvolvedoras

    Projeto desenvolvido para o Hackathon de Dados.

    Sistema Inteligente de Análise de Perfil
Financeiro, Consumo e Geração de Insights Baseado em Dados.


    ### 🤝 Agradecimentos

    - Elas+ Tech
    - Ada Tech
    - Artemisia
    - Caixa
    - Fundo Socioambiental
    """
)

```

# requirements.txt

```txt
streamlit
pandas
numpy
plotly
scikit-learn
matplotlib
```
