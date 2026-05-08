import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import base64
import os
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix

# =========================================================
# CONFIGURAÇÃO E CARREGAMENTO DE IMAGENS
# =========================================================
st.set_page_config(page_title="Inclusão Preditiva | Decision Intelligence", page_icon="📊", layout="wide")

def carregar_imagem_base64(caminho):
    if os.path.exists(caminho):
        with open(caminho, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

logo_base64 = carregar_imagem_base64("logo.png")

# =========================================================
# CSS PREMIUM CUSTOMIZADO (CAIXA + ARTEMISIA)
# =========================================================
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

html, body, [class*="css"] {{ font-family: 'Inter', sans-serif; }}
.stApp {{ background-color: #F8FAFC; }}

/* Sidebar Estilizada */
section[data-testid="stSidebar"] {{
    background: linear-gradient(180deg, #004a99 0%, #003366 100%);
}}
section[data-testid="stSidebar"] * {{ color: white !important; }}

/* Hero Section */
.hero {{
    background: linear-gradient(135deg, #004a99, #00A4E0);
    padding: 50px;
    border-radius: 25px;
    color: white;
    margin-bottom: 30px;
}}
.hero h1 {{ color: white !important; font-size: 44px !important; font-weight: 800 !important; }}
.hero p {{ color: #E0E7FF; font-size: 20px; }}

/* Cards de Conteúdo */
.card {{
    background: white;
    padding: 28px;
    border-radius: 18px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.06);
    border-left: 6px solid #ff7a00;
    margin-bottom: 20px;
}}

.insight {{
    background: #FFF7ED;
    border-left: 8px solid #ff7a00;
    padding: 22px;
    border-radius: 14px;
    color: #9A3412;
}}

.footer {{
    background: #111827;
    color: white;
    padding: 40px;
    border-radius: 20px;
    text-align: center;
    margin-top: 50px;
}}
</style>
""", unsafe_allow_html=True)

# =========================================================
# GERAÇÃO DE DADOS E MODELO (LÓGICA DO PROJETO)
# =========================================================
@st.cache_data
def load_data():
    np.random.seed(42)
    n = 2000
    df = pd.DataFrame({
        "total_gasto": np.random.randint(100, 6000, n),
        "total_pedidos": np.random.randint(1, 20, n),
        "dias_sem_compra": np.random.randint(1, 365, n)
    })
    df["ticket_medio"] = df["total_gasto"] / df["total_pedidos"]
    df["frequencia_compra"] = df["total_pedidos"] / (df["dias_sem_compra"] + 1)
    df["churn"] = np.where(df["dias_sem_compra"] > 120, 1, 0)
    return df

clientes = load_data()

# ML Treinamento rápido para o simulador
X = clientes[["total_gasto", "total_pedidos", "dias_sem_compra", "ticket_medio", "frequencia_compra"]]
y = clientes["churn"]
modelo = LogisticRegression(max_iter=1000).fit(X, y)

# =========================================================
# SIDEBAR NAVEGAÇÃO
# =========================================================
with st.sidebar:
    if logo_base64:
        st.markdown(f'<img src="data:image/png;base64,{logo_base64}" style="width:100%; border-radius: 10px; margin-bottom: 20px;">', unsafe_allow_html=True)
    
    st.markdown("### 📌 Jornada de Decisão")
    pagina = st.radio("", [
        "Home", 
        "Padrões de Consumo", 
        "Inteligência SQL", 
        "Score de Risco (ML)", 
        "Impacto Social"
    ])
    st.markdown("---")
    st.caption("Hackathon: Ada | Elas + Tech | Caixa | Artemisia")

# =========================================================
# PAGINA: HOME
# =========================================================
if pagina == "Home":
    st.markdown("""
    <div class="hero">
        <h1>Sistema Inteligente de Inclusão Financeira</h1>
        <p>Previsão de Evasão e Recomendações Estratégicas para a Retenção de Clientes.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Base de Clientes", f"{len(clientes)}")
    col2.metric("Receita Sob Análise", f"R$ {clientes['total_gasto'].sum()/1e6:.1f}M")
    col3.metric("Taxa de Churn", f"{clientes['churn'].mean():.1%}")
    col4.metric("Ticket Médio", f"R$ {clientes['ticket_medio'].mean():.2f}")

    st.markdown("""
    <div class="card">
        <h2>🎯 O Propósito Social</h2>
        <p>Este projeto une a robustez técnica do <b>Python e SQL</b> com o compromisso de <b>Inclusão Financeira</b> da Caixa. 
        Identificamos sinais de vulnerabilidade antes que o cliente perca o vínculo com o sistema financeiro.</p>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# PAGINA: PADRÕES DE CONSUMO
# =========================================================
elif pagina == "Padrões de Consumo":
    st.title("📈 Padrões de Comportamento")
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        fig1 = px.histogram(clientes, x="dias_sem_compra", color="churn", 
                            title="Distribuição de Inatividade (Recência)",
                            color_discrete_sequence=['#004a99', '#ff7a00'])
        st.plotly_chart(fig1, use_container_width=True)
    
    with col_b:
        fig2 = px.scatter(clientes, x="total_gasto", y="frequencia_compra", color="churn",
                          title="Relação Gasto vs. Frequência",
                          color_discrete_sequence=['#004a99', '#ff7a00'])
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("""
    <div class="insight">
        <b>💡 Insight de Negócio:</b> Clientes que ultrapassam a marca de 120 dias sem compras apresentam 
        uma queda exponencial na probabilidade de retorno sem intervenção ativa.
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# PAGINA: SQL
# =========================================================
elif pagina == "Inteligência SQL":
    st.title("🧠 Camada Analítica SQL")
    
    st.markdown("""
    <div class="card">
        Usamos o <b>DuckDB</b> para transformar dados brutos em tabelas de decisão. 
        Abaixo, a lógica de segmentação por vulnerabilidade financeira.
    </div>
    """, unsafe_allow_html=True)

    st.code("""
    WITH perfil_risco AS (
        SELECT 
            customer_id,
            total_gasto,
            CASE WHEN dias_sem_compra > 90 THEN 'Vulnerável' ELSE 'Saudável' END as status
        FROM olist_consolidado
    )
    SELECT status, AVG(total_gasto) as ticket_medio
    FROM perfil_risco
    GROUP BY 1
    """, language="sql")

# =========================================================
# PAGINA: ML (SIMULADOR)
# =========================================================
elif pagina == "Score de Risco (ML)":
    st.title("🤖 Score de Risco em Tempo Real")
    
    col_input, col_result = st.columns([1, 1.2])
    
    with col_input:
        st.markdown("### Parâmetros do Cliente")
        gasto = st.slider("💰 Gasto Total", 100, 6000, 1000)
        pedidos = st.slider("🛒 Total de Pedidos", 1, 20, 5)
        dias = st.slider("📅 Dias Sem Compra", 0, 365, 60)
    
    with col_result:
        # Lógica de predição
        novo_c = pd.DataFrame([[gasto, pedidos, dias, gasto/pedidos, pedidos/(dias+1)]], 
                             columns=["total_gasto", "total_pedidos", "dias_sem_compra", "ticket_medio", "frequencia_compra"])
        prob = modelo.predict_proba(novo_c)[0][1]
        
        st.markdown("### Probabilidade de Evasão")
        st.title(f"{prob:.1%}")
        
        if prob >= 0.7:
            st.error("🚨 **Risco Alto:** Recomenda-se isenção de tarifas e oferta de microcrédito.")
        elif prob >= 0.3:
            st.warning("⚠️ **Risco Médio:** Enviar conteúdos de educação financeira (Parceria Ada).")
        else:
            st.success("✅ **Cliente Saudável:** Foco em programas de fidelidade.")

# =========================================================
# PAGINA: IMPACTO SOCIAL
# =========================================================
elif pagina == "Impacto Social":
    st.title("🌍 Inclusão e Impacto")
    
    st.markdown("""
    <div class="card">
        <h2>Transformando Churn em Inclusão</h2>
        <p>Ao prever a saída de um cliente de baixa renda, a <b>Caixa</b> pode agir preventivamente 
        garantindo que ele não perca o acesso ao microcrédito e à cidadania financeira. 
        Este é o verdadeiro <b>Decision Intelligence</b>: tecnologia a serviço das pessoas.</p>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# RODAPÉ INTEGRADO
# =========================================================
st.markdown("""
<div class="footer">
    <h3>👩‍💻 Desenvolvido para o Hackathon Decision Intelligence</h3>
    <p>Caixa • Artemisia • Ada Tech • Elas+ Tech</p>
    <small>Stack: Python | SQL | Scikit-Learn | Streamlit</small>
</div>
""", unsafe_allow_html=True)
