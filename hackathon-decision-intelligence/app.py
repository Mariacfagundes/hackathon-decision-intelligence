import streamlit as st
import pandas as pd
import base64
from PIL import Image

# ==========================================
# FUNÇÃO PARA CARREGAR IMAGEM LOCAL (LOGO)
# ==========================================
def get_image_base64(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Tente carregar a sua imagem (ajuste o nome do arquivo conforme necessário)
try:
    img_path = "image_a642b1.png" # Ou "edited-image.png"
    img_base64 = get_image_base64(img_path)
    logo_html = f'<img src="data:image/png;base64,{img_base64}" style="width:100%; border-radius: 10px; margin-bottom: 20px;">'
except:
    logo_html = "" # Fallback caso a imagem não seja encontrada

# ==========================================
# CONFIGURAÇÃO DE DESIGN (CSS AVANÇADO)
# ==========================================
st.set_page_config(page_title="Inclusão Preditiva | Hackathon", layout="wide")

st.markdown(f"""
    <style>
    /* Fundo degradê corporativo */
    .stApp {{
        background: linear-gradient(135deg, #e0eafc 0%, #cfdef3 100%);
    }}
    
    /* Barra Lateral Estilizada */
    [data-testid="stSidebar"] {{
        background-color: #004a99 !important; /* Azul Caixa */
        padding: 20px;
    }}
    
    /* Títulos e Tipografia */
    h1 {{ color: #004a99; font-weight: 800; text-shadow: 1px 1px 2px rgba(0,0,0,0.1); }}
    h2 {{ color: #003366; border-left: 5px solid #ff7a00; padding-left: 15px; }}
    
    /* Estilo de Card para o conteúdo */
    .content-card {{
        background-color: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.1);
        color: #2d3748;
        line-height: 1.6;
        font-size: 1.1rem;
    }}
    
    .highlight {{ color: #ff7a00; font-weight: bold; }}
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# NAVEGAÇÃO POR PÁGINAS (STORYTELLING)
# ==========================================
with st.sidebar:
    st.markdown(logo_html, unsafe_allow_html=True) # SUA LOGO AQUI
    st.markdown("<h2 style='color:white; border:none;'>Menu do Projeto</h2>", unsafe_allow_html=True)
    page = st.radio("", [
        "🏠 O Manifesto", 
        "📊 Inteligência SQL", 
        "📈 Ciência de Dados", 
        "🧠 Modelo Preditivo", 
        "🎯 Ação Estratégica"
    ])
    st.markdown("---")
    st.caption("Hackathon: Ada | Elas + Tech | Caixa | Artemisia")

# ==========================================
# PÁGINA 1: O MANIFESTO
# ==========================================
if page == "🏠 O Manifesto":
    st.title("Sistema Inteligente de Inclusão Financeira")
    
    st.markdown(f"""
    <div class="content-card">
        <h2>Por que a Inclusão Financeira é o nosso Norte?</h2>
        <p>
            Muitas empresas olham para o <b>Churn</b> apenas como perda de faturamento. Mas para a <b>Caixa</b> e a <b>Artemisia</b>, 
            a evasão de um cliente pode significar o fim de um sonho de empreendedorismo ou a perda de acesso a serviços básicos.
            <br><br>
            Nossa solução utiliza <span class='highlight'>Decision Intelligence</span> para entender quem está saindo e, 
            mais importante, <b>como podemos trazê-los de volta</b>. Este não é um projeto de algoritmos, é um projeto de 
            pessoas conectadas por dados.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.image("edited-image.png", caption="Nossa Arquitetura de Impacto", use_column_width=True)

# ==========================================
# PÁGINA 2: INTELIGÊNCIA SQL
# ==========================================
elif page == "📊 Inteligência SQL":
    st.title("A Base: Consultas Analíticas")
    
    st.markdown("""
    <div class="content-card">
        Utilizamos o <b>DuckDB</b> para transformar os datasets da Olist e Telco em inteligência acionável. 
        Segmentamos clientes por faixas de renda e comportamento de consumo para identificar onde a 
        vulnerabilidade financeira é maior.
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("Análise de Ticket Médio por Perfil")
    # Simulação de dados para visualização
    df_sql = pd.DataFrame({'Perfil': ['Baixa Renda', 'Média', 'Alta'], 'Evasão (%)': [92, 85, 70]})
    st.bar_chart(df_sql.set_index('Perfil'))

# ==========================================
# PÁGINA 3: CIÊNCIA DE DADOS
# ==========================================
elif page == "📈 Ciência de Dados":
    st.title("Rigor Estatístico e Probabilidade")
    
    st.markdown("""
    <div class="content-card">
        Aplicamos probabilidade condicional para entender os gatilhos da evasão. 
        Não olhamos apenas para o passado; calculamos a <b>Probabilidade de Risco</b> para agir antes que o 
        vínculo financeiro seja quebrado.
    </div>
    """, unsafe_allow_html=True)
    
    # Exemplo de gráfico de dispersão
    st.markdown("### Correlação: Tempo de Conta vs. Gastos")
    st.info("Aqui mostramos que clientes com menor tempo de casa precisam de incentivos de microcrédito imediatos.")

# ==========================================
# PÁGINA 4: MODELO PREDITIVO
# ==========================================
elif page == "🧠 Modelo Preditivo":
    st.title("Machine Learning: Regressão Logística")
    
    st.markdown("""
    <div class="content-card">
        Nosso "cérebro" classifica o risco em tempo real. O modelo gera um <b>Score de Risco (0 a 100)</b>, 
        permitindo que a equipe de retenção saiba exatamente onde investir energia.
    </div>
    """, unsafe_allow_html=True)
    
    val = st.slider("Simule o risco de um cliente:", 0, 100, 85)
    if val > 80:
        st.error(f"ALERTA: Risco Crítico ({val}%). Sugestão: Oferta de Isenção de Tarifas.")
    else:
        st.success(f"Estável: Risco Baixo ({val}%). Sugestão: Programa de Pontos.")

# ==========================================
# PÁGINA 5: AÇÃO ESTRATÉGICA
# ==========================================
elif page == "🎯 Ação Estratégica":
    st.title("O Impacto Final: Recomendações")
    
    st.markdown("""
    <div class="content-card">
        <h2>Pronto para a Contratação</h2>
        <p>
            Unimos o suporte da <b>Ada</b>, a visão da <b>Artemisia</b> e a capilaridade da <b>Caixa</b>. 
            Nossas recomendações são focadas em manter o brasileiro incluído no sistema financeiro.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.info("### Inclusão Feminina\nPromoções específicas para microempreendedoras (Elas + Tech).")
    with col_b:
        st.warning("### Educação Financeira\nTrilhas de aprendizado para reduzir o endividamento.")
