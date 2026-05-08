# 🧠 Decision Intelligence — Previsão de Churn e Recomendações Estratégicas de Retenção

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-F7931E?style=for-the-badge&logo=scikit-learn)
![DuckDB](https://img.shields.io/badge/DuckDB-SQL-yellow?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit)

</div>

---

> Projeto de conclusão de curso desenvolvido na **Hackathon Elas+ Tech**, promovida pela **Ada Tech** em parceria com a **Caixa Econômica Federal** e a **Artemísia**.

---

## 📌 Sobre o Projeto

Este projeto propõe uma solução completa de **Decision Intelligence** para análise de perfil financeiro e previsão de evasão de clientes (churn). A partir de dados reais dos ecossistemas de **e-commerce** e **telecomunicações**, desenvolvemos um sistema capaz de identificar quais clientes estão em risco de cancelamento, classificá-los por nível de risco e recomendar ações estratégicas de retenção.

Quando um cliente para de comprar, raramente é do nada. Os sinais estão nos dados e este projeto foi construído para encontrá-los.

---

## 🎯 Objetivos

- Prever o risco de churn de clientes com base em comportamento de consumo
- Analisar padrões financeiros e de frequência de compra
- Gerar um score de risco individual (0 a 100) para cada cliente
- Classificar clientes em faixas de risco: **Crítico, Alto, Médio e Baixo**
- Recomendar ações estratégicas de retenção por perfil de risco
- Disponibilizar os insights em um dashboard interativo

---

## 🏗️ Arquitetura da Solução

```
Datasets CSV (Olist + Telco)
        ↓
Python / Pandas — Limpeza e tratamento dos dados
        ↓
DuckDB / SQL — Consultas analíticas e segmentações
        ↓
EDA + Estatística — Insights e probabilidades condicionais
        ↓
Machine Learning — Predição de churn (Regressão Logística)
        ↓
Streamlit — Dashboard interativo com recomendações
```

---

## 🗂️ Estrutura dos Dados

### Dataset Olist (E-commerce Brasileiro)
Utilizado para análise de comportamento de consumo e criação da variável churn com base em inatividade de compra (> 90 dias).

| Arquivo | Descrição |
|---|---|
| `olist_orders_dataset.csv` | Informações dos pedidos |
| `olist_order_items_dataset.csv` | Itens comprados em cada pedido |
| `olist_customers_dataset.csv` | Dados dos clientes |
| `olist_order_payments_dataset.csv` | Informações de pagamento |
| `olist_products_dataset.csv` | Dados dos produtos |
| `product_category_name_translation.csv` | Tradução das categorias |

🔗 [Dataset Olist no Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

### Dataset Telco Customer Churn
Utilizado para análise de churn em contexto de telecomunicações, com variáveis ricas como tipo de contrato, serviços contratados e tempo de permanência.

🔗 [Dataset Telco no Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

---

## 🧹 Limpeza e Tratamento dos Dados

- Tratamento de valores nulos
- Conversão de variáveis numéricas
- Integração de múltiplas tabelas via merge
- Criação da variável **churn** (inatividade > 90 dias)
- Construção de métricas comportamentais por cliente
- Padronização de tipos de dados
- Criação de tabelas analíticas agregadas por cliente

---

## 🗃️ SQL na Prática

Foram utilizadas consultas SQL avançadas com **DuckDB** para geração de insights analíticos e segmentações estratégicas, incluindo:

- Churn por perfil de gasto
- Churn por faixa de renda
- Ticket médio por segmento
- Frequência de compra
- Consumo por categoria de produto
- Ranking de clientes por comportamento

**Técnicas SQL utilizadas:** `WITH (CTE)`, `CASE WHEN`, `GROUP BY`, `WINDOW FUNCTIONS`, `RANK()`, `NTILE()`

---

## 📊 Estatística e Análise Exploratória

Foi realizada análise estatística descritiva completa para identificação de padrões de comportamento, contemplando:

- Média, mediana e desvio padrão
- Distribuição de churn (89,94% de churn na base Olist)
- Análise de frequência de compra
- Comparação de gasto médio entre clientes ativos e em churn
- Distribuição de dias sem compra
- Visualizações interativas com Plotly

**Principal achado:** o gasto médio entre clientes ativos (R$ 144,86) e em churn (R$ 148,20) é praticamente idêntico — o valor gasto não é um preditor relevante de churn. O tempo de inatividade é o sinal mais determinante.

---

## 🎲 Probabilidade Condicional

Foram aplicadas análises de probabilidade condicional para identificar segmentos com maior risco de evasão:

| Cenário | P(churn) |
|---|---|
| Contrato Mensal | 85% |
| Sem Suporte Técnico | 76% |
| Internet Fibra Óptica | 69% |
| Boleto Bancário | 52% |

**Conclusão:** clientes com contrato mensal representam o maior risco de churn, independentemente do valor gasto.

---

## 🤖 Machine Learning

Foi desenvolvido um modelo preditivo de **Regressão Logística** para previsão de churn, com as seguintes etapas:

1. Separação treino/teste
2. Treinamento do modelo
3. Geração de probabilidades de churn por cliente
4. Criação do score de risco (0 a 100)
5. Classificação em faixas: Crítico, Alto, Médio e Baixo
6. Geração de recomendações estratégicas por perfil

### Métricas do Modelo
| Métrica | Resultado |
|---|---|
| Recall | 81,5% |
| Accuracy | - |
| Precision | - |

### Recomendações por Faixa de Risco
| Faixa | Score | Recomendação |
|---|---|---|
| 🔴 Crítico | ≥ 80 | Oferta agressiva de retenção |
| 🟠 Alto | ≥ 60 | Contato preventivo |
| 🟡 Médio | ≥ 40 | Campanha de engajamento |
| 🟢 Baixo | < 40 | Cliente estável |

### Variáveis Mais Importantes
A **Recência** (tempo desde a última interação) foi a variável mais determinante para o modelo, seguida pelo tipo de **Contrato**.

---

## 📱 Dashboard Streamlit

O dashboard foi desenvolvido em Streamlit com visualizações interativas, apresentando:

- Indicadores de churn
- Score de risco por cliente
- Segmentações por perfil de risco
- Análises de probabilidade condicional
- Importância das variáveis do modelo
- Recomendações estratégicas de retenção

🔗 [Acessar Dashboard](#) *(link a ser inserido)*

---



## 🛠️ Tecnologias Utilizadas

| Tecnologia | Uso |
|---|---|
| Python | Processamento e análise de dados |
| Pandas | Manipulação de DataFrames |
| DuckDB | Consultas SQL analíticas |
| Plotly | Visualizações interativas |
| Scikit-learn | Modelo preditivo de Machine Learning |
| Streamlit | Dashboard interativo |
| Google Colab | Ambiente de desenvolvimento |

---

## 👩‍💻 Time

Projeto desenvolvido com 💜 pelo **Grupo 8** da Hackathon Elas+ Tech:

| Nome |
|---|
| Barbara Andrade de Rossi |
| Lauren Oliveira |
| Leide Dias |
| Maria Clara Fagundes |
| Naida Martins |

---

## 🏆 Sobre a Hackathon

Este projeto foi desenvolvido como trabalho de conclusão do curso de **Ciência de Dados** da **Ada Tech**, no contexto da **Hackathon Elas+ Tech**, realizada em parceria com a **Caixa Econômica Federal** e a **Artemísia**.

---

<div align="center">
  <sub>Desenvolvido com 💜 por mulheres na tecnologia</sub>
</div>
