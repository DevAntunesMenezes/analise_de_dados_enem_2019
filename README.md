# 📊 Análise de Desempenho Educacional – ENEM 2019

Este projeto apresenta uma análise do desempenho dos participantes do **ENEM 2019**, com foco em **visualização de dados educacionais**, comparação entre perfis de estudantes e interpretação de indicadores de desempenho.

O objetivo principal é explorar os dados de forma clara e organizada, utilizando **Python para tratamento mínimo dos dados** e **Power BI para análise e visualização interativa**.

---

## 🎯 Objetivos do Projeto

- Analisar o desempenho médio dos estudantes no ENEM 2019  
- Comparar resultados por:
  - Estado (UF)
  - Sexo
  - Rede de ensino (Pública, Privada, Outros)
- Avaliar o desempenho por área do conhecimento
- Identificar o percentual de estudantes com **alto desempenho (≥ 650 pontos)**  
- Desenvolver um dashboard claro, funcional e adequado para portfólio

---

## 🧩 Estrutura do Projeto

```
enem_2019_projeto/
│
├── dados_brutos/
│   └── enem_2019.csv
│
├── dados_tratados/
│   └── enem_fato.csv
│
├── scripts/
│   └── tratamento_minimo.py
│
├── dashboard/
│   └── enem_2019.pbix
│
└── README.md
```

---

## 🛠️ Ferramentas Utilizadas

- **Python**
  - Pandas
  - NumPy
- **Power BI Desktop**
- **Git & GitHub**

---

## 🔄 Pipeline de Dados

1. Dados brutos obtidos a partir do ENEM 2019 (INEP)  
2. Tratamento mínimo em Python (limpeza, seleção de colunas e correção de escala)  
3. Exportação de uma única tabela fato  
4. Análise e visualização no Power BI com métricas calculadas via DAX  

---

## 📈 Principais Métricas e Análises

- Total de participantes  
- Média geral do ENEM  
- Média por área do conhecimento  
- Comparações por estado, sexo e rede de ensino  
- Percentual de estudantes com desempenho ≥ 650 pontos  

---

## 🎨 Dashboard

O dashboard foi desenvolvido em **uma única página**, contendo:

- Painel lateral de filtros  
- KPIs principais no topo  
- Gráficos comparativos e analíticos  

*(Inserir imagens do dashboard aqui)*

---

## ℹ️ Observações

Este projeto foi desenvolvido **integralmente no Power BI Desktop**, por decisão de escopo.

Algumas funcionalidades disponíveis apenas no **Power BI Service** não foram incluídas, mantendo o projeto totalmente funcional em ambiente local e independente de conta institucional.

---

## 📚 Fonte dos Dados

- **INEP – Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira**
- Microdados do ENEM 2019

---

## 👤 Autor

**Antunes Menezes**  
Professor de Matemática | Análise de Dados Educacionais  

---

Projeto desenvolvido para fins de estudo e portfólio.
