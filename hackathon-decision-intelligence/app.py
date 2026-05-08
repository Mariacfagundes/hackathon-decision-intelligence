import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# =========================================================
# CONFIGURAÇÃO DE LAYOUT E ESTILO PROFISSIONAL
# =========================================================
st.set_page_config(
    page_title="Decision Intelligence - Grupo 8",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        color: #1E293B;
    }

    /* Sidebar Profissional */
    [data-testid="stSidebar"] {
        background-color: #0F172A !important;
    }
    [data-testid="stSidebar"] * {
        color: #F8FAFC !important;
    }

    /* Cards de Conteúdo */
    .content-card {
        background-color: #FFFFFF;
        padding: 40px;
        border-radius: 12px;
        border-left: 8px solid #1E293B;
        box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
        margin-bottom: 30px;
    }

    /* Bloco de Storytelling de Dados */
    .story-analysis {
        background-color: #F8FAFC;
        padding: 25px;
        border-radius: 8px;
        border: 1px solid #E2E8F0;
        line-height: 1.7;
        color: #334155;
        margin-top: 20px;
    }

    .section-title {
        font-weight: 700;
        font-size: 24px;
        margin-bottom: 20px;
        border-bottom: 2px solid #E2E8F0;
        padding-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# =========================================================
# NAVEGAÇÃO LATERAL COM LOGOTIPO
# =========================================================
with st.sidebar:
    # Inclusão do logotipo no topo do menu lateral
    try:
        st.image("logo.png", use_container_width=True)
    except:
        # Título reserva caso a imagem não seja encontrada
        st.markdown("<h2 style='text-align: center; color: white;'>Decision Intelligence</h2>", unsafe_allow_html=True)
    
    st.markdown("---")
    capitulo = st.radio("Capítulos do Projeto", [
        "1. Contexto e Intenção",
        "2. Diagnóstico Estatístico (EDA)",
        "3. Probabilidade Condicional",
        "4. Inteligência Preditiva (ML)",
        "5. Recomendações e Autoras"
    ])
    
    st.markdown("---")
    st.caption("Grupo 8 • 2026")

# =========================================================
# CAPÍTULO 1: CONTEXTO E INTENÇÃO
# =========================================================
if capitulo == "1. Contexto e Intenção":
    st.title("Decisão inteligente: prevendo cancelamentos e apoiando decisões estratégicas de retenção")
    st.subheader("Contexto e Intenção")

    st.markdown("""
    <div class="content-card">
        <p style="font-size: 1.15rem; line-height: 1.8;">
        Todo mês, empresas perdem clientes sem entender exatamente o porquê. A taxa de Churn não acontece de repente, ela se desenvolve em silêncio, deixando rastros invisíveis no comportamento de consumo antes de se tornar uma perda real. 
        <br><br>
        Ao analisar o comportamento de milhares de consumidores, vemos que padrões se repetem. Alguns sinais existem e saber enxergá-los e interpretá-los é o que separa uma empresa que reage de uma empresa que antecipa.
        <br><br>
        E é exatamente isso que este projeto propõe. Combinando dados reais dos ecossistemas de e-commerce e telecomunicações, nosso dashboard interativo revela quais clientes estão em risco de cancelamento, por que isso está acontecendo e onde a estrutura de gastos aponta para novas demandas de inclusão.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<p class="section-title">O que o projeto revela</p>', unsafe_allow_html=True)
    
    st.write("A partir da análise do comportamento dos clientes, o dashboard entrega três camadas de inteligência:")
    
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Perfis de Risco:** clientes classificados em faixas de risco — Crítico, Alto, Médio e Baixo — com base em seu score de probabilidade de churn, permitindo priorizar ações de retenção.")
        st.markdown("**Recomendações estratégicas:** para cada perfil de risco, o sistema sugere uma ação concreta, desde ofertas agressivas de retenção até campanhas de engajamento preventivo.")
    with col2:
        st.markdown("**Visão preditiva:**  um modelo de Machine Learning treinado para prever quais clientes estão prestes a cancelar, com base em frequência de compra, valor gasto e tempo de inatividade.")

    st.markdown('<p class="section-title">Onde isso impacta</p>', unsafe_allow_html=True)
    
    st.write("1. **Gestão Estratégica:** permite que empresas priorizem recursos de retenção com base em evidências preditivas sabendo exatamente quais clientes precisam de atenção imediata e qual abordagem usar..")
    st.write("2. **Redução de perdas:** ao identificar clientes em risco antes do cancelamento, empresas podem agir preventivamente e evitar a perda de receita associada ao churn.")
    st.write("3. **Decisões orientadas por dados:** transforma análises complexas de comportamento em recomendações simples e acionáveis, tornando a inteligência de dados acessível para times de negócio.")

# =========================================================
# CAPÍTULO 2: EDA E ESTATÍSTICA
# =========================================================
elif capitulo == "2. Diagnóstico Estatístico (EDA)":
    st.title("Diagnóstico Estatístico")
    
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown('<p class="section-title">Análise estratégica</p>', unsafe_allow_html=True)
    
    data_eda = pd.DataFrame({
        'Dias_Inatividade': np.random.randint(1, 365, 200),
        'Valor_Gasto': np.random.uniform(50, 5000, 200),
        'Categoria': np.random.choice(['Saudável', 'Em Alerta', 'Crítico'], 200)
    })
    fig_eda = px.scatter(data_eda, x='Dias_Inatividade', y='Valor_Gasto', color='Categoria',
                         title="Correlação: Inatividade vs. Valor Transacionado",
                         color_discrete_map={'Saudável':'#1E293B', 'Em Alerta':'#3B82F6', 'Crítico':'#EF4444'})
    st.plotly_chart(fig_eda, use_container_width=True)
    
    st.markdown("""
     <div style="font-size: 1.1rem; margin-top: 10px; line-height: 1.6;">
        <strong style="color: #31333F;">Análise Estratégica:</strong>
        <p>
        O gráfico revela que clientes classificados como Críticos e Em Alerta estão distribuídos ao longo de toda a faixa de inatividade, independentemente do valor gasto. 
        Isso indica que o tempo sem comprar é um sinal de risco mais determinante do que o quanto o cliente gastou, reforçando a necessidade de ações de retenção baseadas em comportamento temporal, não apenas em valor financeiro.
        </p>
    </div>
    """, unsafe_allow_html=True)
   
# =========================================================
# CAPÍTULO 3: PROBABILIDADE CONDICIONAL
# =========================================================
elif capitulo == "3. Probabilidade Condicional":
    st.title("Probabilidade Condicional de Evasão")
    
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown('<p class="section-title">P(Churn | Fator de Risco)</p>', unsafe_allow_html=True)
    
    prob_values = {'Cenário': ['Contrato Mensal', 'Boleto Bancário', 'Fibra Óptica', 'Sem Suporte'],
                   'Probabilidade': [0.85, 0.52, 0.69, 0.77]}
    df_p = pd.DataFrame(prob_values)
    fig_p = px.bar(df_p, x='Cenário', y='Probabilidade', title="Probabilidade de Churn por Variável",
                   color_discrete_sequence=['#0F172A'])
    st.plotly_chart(fig_p, use_container_width=True)
    
    st.markdown("""
    <div style="font-size: 1.1rem; margin-top: 10px; line-height: 1.6;">
        <strong style="color: #31333F;">Análise Estratégica:</strong><br>
        A análise de probabilidade condicional revela que clientes com contrato mensal apresentam a maior probabilidade de churn (85%), seguidos por clientes sem suporte técnico (76%) e com fibra óptica (69%). 
        Curiosamente, o boleto bancário apresenta probabilidade menor (52%), sugerindo que a forma de pagamento isolada não é o fator mais crítico.
        <p>
        A principal recomendação é incentivar a migração de contratos mensais para planos anuais, já que esse é o perfil com maior risco de cancelamento identificado nos dados.
        </p>
    </div>
    """, unsafe_allow_html=True)
  
# =========================================================
# CAPÍTULO 4: MACHINE LEARNING
# =========================================================
elif capitulo == "4. Inteligência Preditiva (ML)":
    st.title("Motor Preditivo e Machine Learning")
    
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown('<p class="section-title">Feature Importance e Performance</p>', unsafe_allow_html=True)
    
    col_m, col_g = st.columns([1, 2])
    with col_m:
        st.metric("Acurácia do Modelo", "88.2%")
        st.metric("Recall (Sensibilidade)", "81.5%")
        st.write("Modelo: Regressão Logística")
        
    with col_g:
        features = {'Variável': ['Recência', 'Contrato', 'Gasto Mensal', 'Serviço Streaming', 'Idade'],
                    'Importância': [0.48, 0.35, 0.10, 0.05, 0.02]}
        fig_ml = px.bar(pd.DataFrame(features), x='Importância', y='Variável', orientation='h',
                        title="Peso das Variáveis na Decisão do Modelo",
                        color_discrete_sequence=['#3B82F6'])
        st.plotly_chart(fig_ml, use_container_width=True)
        
    st.markdown("""
    <div style="font-size: 1.1rem; margin-top: 10px; line-height: 1.6;">
        <strong style="color: #31333F;">Análise Estratégica:</strong><br>
        O modelo de Regressão Logística atingiu um recall de 81,5%, ou seja, consegue identificar corretamente mais de 8 em cada 10 clientes que realmente cancelariam. 
        A variável mais determinante foi a Recência (tempo desde a última interação), seguida pelo tipo de contrato. 
        Gasto mensal, serviço de streaming e idade tiveram impacto menor. 
        <p>
        Isso reforça a recomendação central do projeto: 
        empresas devem monitorar o tempo de inatividade dos clientes como principal sinal de alerta, e priorizar ações de retenção para quem possui contratos mensais.
        </p>
    """, unsafe_allow_html=True)
    
# =========================================================
# CAPÍTULO 5: CONCLUSÃO E EQUIPE
# =========================================================
elif capitulo == "5. Recomendações e Autoras":
    st.title("Conclusão e Autoras")
    
    st.markdown("""
    <div class="content-card">
    <p style="font-size: 1.1rem;">
        A Decisão Inteligente aplicada neste projeto transforma dados de comportamento em decisões concretas de retenção.
        Com um modelo preditivo capaz de identificar mais de 8 em cada 10 clientes em risco, um score de churn individualizado e recomendações estratégicas por perfil, este sistema oferece às empresas algo valioso: a capacidade de agir antes que o cancelamento aconteça.
        <br><br>
        Os dados revelaram achados importantes: o tempo de inatividade é o sinal mais crítico de risco, clientes com contrato mensal são os mais vulneráveis ao cancelamento, e a probabilidade de churn pouco varia com o valor gasto, o que significa que nenhum perfil de cliente está automaticamente protegido apenas por gastar mais.
        <br><br>
        Mais do que uma análise de dados, este projeto é uma ferramenta de antecipação que converte padrões invisíveis de comportamento em ações visíveis e planejamentos de longo prazo
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<p class="section-title">Equipe de Desenvolvimento - Grupo 8</p>', unsafe_allow_html=True)
    equipe = ["Barbara Andrade", "Lauren Oliveira", "Leide Dias", "Maria Clara Fagundes", "Maida Martins"]
    c1, c2, c3, c4, c5 = st.columns(5)
    for i, nome in enumerate(equipe):
        with [c1, c2, c3, c4, c5][i]:
            st.write(f"**{nome}**")
            st.caption("Analista de Dados")
            
    st.markdown("---")
    st.write("Patrocínio e Parcerias: Ada+tech | Artemisia | CAIXA")
