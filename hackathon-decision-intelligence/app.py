import streamlit as st

st.set_page_config(
    page_title="Decision Intelligence",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Decision Intelligence")
st.subheader("Sistema Inteligente de Previsão de Churn")

st.markdown("""
Projeto desenvolvido para análise de perfil financeiro,
consumo e previsão de evasão de clientes utilizando:

- Python
- SQL
- Machine Learning
- Streamlit
""")

col1, col2, col3 = st.columns(3)

col1.metric("Clientes", "70.043")
col2.metric("Taxa de Churn", "26.5%")
col3.metric("Modelo ML", "Logistic Regression")

st.header("🎯 Objetivo do Projeto")

st.write("""
O sistema utiliza técnicas de análise de dados e
Machine Learning para prever risco de churn e gerar
insights estratégicos para retenção de clientes.
""")
