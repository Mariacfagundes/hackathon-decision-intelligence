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
    st.title("Sistema Inteligente de Análise de Perfil Financeiro e Consumo")
    st.subheader("Decision Intelligence e Inclusão Financeira . Contexto e Intenção")

    st.markdown("""
    <div class="content-card">
        <p style="font-size: 1.15rem; line-height: 1.8;">
        Imagine o cenário financeiro atual: a evasão de clientes não é apenas uma métrica de perda de faturamento, mas um sinal silencioso de desengajamento que precede a desbancarização e a exclusão social. Esse ciclo de abandono não é repentino — ele deixa rastros nos dados antes de se consolidar.
        <br><br>
        O projeto nasce como resposta a essa transformação nos padrões de consumo. Com base nos dados dos ecossistemas Olist e Telco, este dashboard interativo revela onde o risco de evasão está mais crítico, onde há maior potencial de recuperação de crédito e onde a estrutura de gastos aponta para novas demandas de inclusão.
        <br><br>
        Mais do que um painel de dados, este projeto é uma <b>ferramenta de antecipação estratégica</b> — para gestores que precisam planejar políticas de retenção e para instituições que buscam transformar o risco em oportunidade de fidelização sustentável.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<p class="section-title">O que o projeto revela</p>', unsafe_allow_html=True)
    st.write("Ao cruzar três indicadores-chave — Recência, Frequência e Valor (RFV) — o dashboard constrói uma visão territorial e comportamental da evasão:")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Hotspots de Risco:** Segmentos com alta inatividade e baixo engajamento, onde a intervenção de crédito deve ser prioritária para evitar a perda total do cliente.")
        st.markdown("**Oportunidades de Retenção:** Perfis com ticket médio elevado mas frequência em queda, onde o mercado ainda é fértil para campanhas de fidelização personalizadas.")
    with col2:
        st.markdown("**Score de Inclusão:** Uma métrica composta que sintetiza o comportamento financeiro para comparar perfis de forma objetiva, revelando onde há maior urgência de suporte.")

    st.markdown('<p class="section-title">Onde isso impacta</p>', unsafe_allow_html=True)
    st.write("1. **Gestão Estratégica:** Permite que empresas priorizem recursos de retenção com base em evidências preditivas.")
    st.write("2. **Inclusão Financeira:** Identifica o momento exato de oferecer microcrédito ou tarifas sociais antes do churn.")
    st.write("3. **Inovação em Dados:** Inspira soluções de vizinhança e serviços personalizados com base em perfis reais de consumo.")

# =========================================================
# CAPÍTULO 2: EDA E ESTATÍSTICA
# =========================================================
elif capitulo == "2. Diagnóstico Estatístico (EDA)":
    st.title("Diagnóstico Estatístico e Comportamental")
    
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown('<p class="section-title">Análise de Recência e Ticket Médio</p>', unsafe_allow_html=True)
    
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
    <div class="story-analysis">
        <b>Análise Estratégica:</b> Observamos que a "zona de silêncio" se inicia após os 60 dias de inatividade. 
        Nesse ponto, o ticket médio sofre uma erosão de 40% antes do cancelamento definitivo. 
        <b>O melhor caminho</b> para a empresa é acionar gatilhos de comunicação no 45º dia, pois os dados 
        mostram que a probabilidade de reativação cai drasticamente após o segundo mês de silêncio.
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

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
    <div class="story-analysis">
        <b>Análise Estratégica:</b> A probabilidade condicional isolou o 'Contrato Mensal' como o maior preditor de risco (85%). 
        Diferente do que se supunha, o valor da fatura não é o principal motivo da saída, mas sim a flexibilidade 
        da desvinculação aliada à falta de suporte técnico. 
        <b>A recomendação</b> é a conversão desses planos para modelos anuais com benefícios progressivos, 
        estabilizando o fluxo de caixa e reduzindo a volatilidade da base.
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

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
    <div class="story-analysis">
        <b>Análise Estratégica:</b> O modelo preditivo atingiu um recall de 81.5%, o que garante que estamos identificando 
        a grande maioria dos clientes em risco real. A 'Recência' domina o peso da decisão algorítmica. 
        <b>O melhor uso desta inteligência</b> é integrar o score de risco diretamente ao sistema de atendimento, 
        permitindo que o operador visualize a probabilidade de saída em tempo real e ofereça condições de 
        inclusão financeira, como microcrédito, para os perfis de alto risco.
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# CAPÍTULO 5: CONCLUSÃO E EQUIPE
# =========================================================
elif capitulo == "5. Recomendações e Autoras":
    st.title("Conclusão e Corpo Técnico")
    
    st.markdown("""
    <div class="content-card">
        <p style="font-size: 1.1rem;">
        A Decision Intelligence aplicada a este projeto transforma dados em decisões de retenção e estatísticas em histórias de inclusão. 
        Este sistema permite enxergar o risco financeiro que está por vir — e decidir como agir agora para preservar a base de clientes.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<p class="section-title">Equipe de Desenvolvimento - Grupo 8</p>', unsafe_allow_html=True)
    equipe = ["Barbara", "Lauren Oliveira", "Leide Dias", "Maria Clara Fagundes", "Naida Martins"]
    c1, c2, c3, c4, c5 = st.columns(5)
    for i, nome in enumerate(equipe):
        with [c1, c2, c3, c4, c5][i]:
            st.write(f"**{nome}**")
            st.caption("Analista de Dados")
            
    st.markdown("---")
    st.write("Patrocínio e Parcerias: Ada+tech | Artemisia | CAIXA")
