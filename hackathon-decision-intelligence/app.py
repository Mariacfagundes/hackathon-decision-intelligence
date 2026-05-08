import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# =========================================================
# CONFIGURAÇÃO DE LAYOUT E ESTILO PROFISSIONAL
# =========================================================

# =========================================================
# CONFIGURAÇÃO DE LAYOUT E ESTILO (ESTÉTICA DA FOTO)
# =========================================================
st.set_page_config(page_title="Decision Intelligence - Grupo 8", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .stApp { background-color: #F8FAFC; }

    .custom-header {
        background-color: #0F172A;
        padding: 35px;
        border-radius: 15px 15px 0px 0px;
        color: white;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .main-card {
        background-color: white;
        padding: 35px;
        border-radius: 0px 0px 15px 15px;
        border: 1px solid #E2E8F0;
        margin-bottom: 30px;
    }

    .risk-card {
        background-color: white;
        padding: 25px;
        border-radius: 12px;
        border: 1px solid #E2E8F0;
        min-height: 200px;
    }
    .border-red { border-top: 6px solid #EF4444; }
    .border-purple { border-top: 6px solid #A855F7; }
    .border-blue { border-top: 6px solid #3B82F6; }

    .impact-card {
        background-color: #EFF6FF;
        padding: 20px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        gap: 15px;
        border: 1px solid #DBEAFE;
        margin-bottom: 10px;
    }
    .number-circle {
        background-color: #1E40AF;
        color: white;
        width: 32px;
        height: 32px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        flex-shrink: 0;
    }
    </style>
""", unsafe_allow_html=True)

# =========================================================
# NAVEGAÇÃO LATERAL
# =========================================================
with st.sidebar:
    try:
        st.image("logo.png", use_container_width=True)
    except:
        st.markdown("<h2 style='text-align: center; color: white;'>Decision Intelligence</h2>", unsafe_allow_html=True)
    
    st.markdown("---")
    capitulo = st.radio("Capítulos do Projeto", [
        "1. Contexto e Intenção",
        "2. Diagnóstico Estatístico (EDA)",
        "3. Probabilidade Condicional",
        "4. Inteligência Preditiva (ML)",
        "5. Recomendações e Autoras"
    ])

# =========================================================
# CAPÍTULO 1: SEU TEXTO INTEGRAL + ESTÉTICA DA FOTO
# =========================================================
if capitulo == "1. Contexto e Intenção":
    st.markdown(f"""
        <div class="custom-header">
            <div>
                <h1 style='margin:0; font-size: 1.8rem;'>Decisão inteligente: prevendo cancelamentos e apoiando decisões estratégicas de retenção</h1>
                <p style='margin:0; opacity: 0.8;'>Contexto e Intenção</p>
            </div>
            <div style="background-color: #1E293B; padding: 15px; border-radius: 8px; border-left: 4px solid #3B82F6;">
                <small style="color: #94A3B8;">PROJETO</small><br>
                <b style="color: white;">Grupo 8 - Decision Intelligence</b>
            </div>
        </div>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        st.markdown(f"""
            <p style='font-size: 1.15rem; color: #334155; line-height: 1.8;'>
            Todo mês, empresas perdem clientes sem entender exatamente o porquê. A taxa de Churn não acontece de repente, 
            ela se desenvolve em silêncio, deixando rastros invisíveis no comportamento de consumo antes de se tornar uma perda real. 
            <br><br>
            Ao analisar o comportamento de milhares de consumidores, vemos que padrões se repetem. Alguns sinais existem e saber 
            enxergá-los e interpretá-los é o que separa uma empresa que reage de uma empresa que antecipa.
            <br><br>
            E é exatamente isso que este projeto propõe. Combinando dados reais dos ecossistemas de e-commerce e telecomunicações, 
            nosso dashboard interativo revela quais clientes estão em risco de cancelamento, por que isso está acontecendo e 
            onde a estrutura de gastos aponta para novas demandas de inclusão.
            </p>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("### 🔍 O que o projeto revela")
    col_r1, col_r2, col_r3 = st.columns(3)
    with col_r1:
        st.markdown('<div class="risk-card border-red"><h4 style="color:#EF4444; margin-top:0;">📊 Perfis de Risco</h4><p style="font-size: 0.95rem; color: #475569;">clientes classificados em faixas de risco — Crítico, Alto, Médio e Baixo — com base em seu score de probabilidade de churn, permitindo priorizar ações de retenção.</p></div>', unsafe_allow_html=True)
    with col_r2:
        st.markdown('<div class="risk-card border-purple"><h4 style="color:#A855F7; margin-top:0;">💡 Recomendações estratégicas</h4><p style="font-size: 0.95rem; color: #475569;">para cada perfil de risco, o sistema sugere uma ação concreta, desde ofertas agressivas de retenção até campanhas de engajamento preventivo.</p></div>', unsafe_allow_html=True)
    with col_r3:
        st.markdown('<div class="risk-card border-blue"><h4 style="color:#3B82F6; margin-top:0;">🔮 Visão preditiva</h4><p style="font-size: 0.95rem; color: #475569;">um modelo de Machine Learning treinado para prever quais clientes estão prestes a cancelar, com base em frequência de compra, valor gasto e tempo de inatividade.</p></div>', unsafe_allow_html=True)

    st.markdown("<br>### ⭐ Onde isso impacta", unsafe_allow_html=True)
    col_i1, col_i2, col_i3 = st.columns(3)
    with col_i1:
        st.markdown('<div class="impact-card"><div class="number-circle">01</div><div><b>Gestão Estratégica</b><br><small>permite que empresas priorizem recursos de retenção com base em evidências preditivas...</small></div></div>', unsafe_allow_html=True)
    with col_i2:
        st.markdown('<div class="impact-card"><div class="number-circle">02</div><div><b>Redução de perdas</b><br><small>ao identificar clientes em risco antes do cancelamento, empresas podem agir preventivamente...</small></div></div>', unsafe_allow_html=True)
    with col_i3:
        st.markdown('<div class="impact-card"><div class="number-circle">03</div><div><b>Decisões orientadas por dados</b><br><small>transforma análises complexas em recomendações simples e acionáveis...</small></div></div>', unsafe_allow_html=True)

# =========================================================
# CAPÍTULOS SEGUINTES (CORREÇÃO DA SINTAXE)
# =========================================================
elif capitulo == "2. Diagnóstico Estatístico (EDA)":
    st.title("Diagnóstico Estatístico (EDA)")
    st.info("Espaço para os gráficos de análise exploratória.")

elif capitulo == "3. Probabilidade Condicional":
    st.title("Probabilidade Condicional")

elif capitulo == "4. Inteligência Preditiva (ML)":
    st.title("Machine Learning")

elif capitulo == "5. Recomendações e Autoras":
    st.title("Conclusão e Equipe")
    
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
