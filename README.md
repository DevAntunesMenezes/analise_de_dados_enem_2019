# 📊 Análise de Desempenho Educacional – ENEM 2019

Este projeto apresenta uma análise do desempenho dos participantes do **ENEM 2019**, com foco em **visualização de dados educacionais**, comparação entre perfis de estudantes e interpretação de indicadores de desempenho.

O objetivo principal é explorar os dados de forma clara e organizada, utilizando **Python para tratamento mínimo dos dados** e **Power BI para análise e visualização interativa**, com foco em portfólio.

---

## 🎯 Objetivos do Projeto

- Analisar o desempenho médio dos estudantes no ENEM 2019  
- Comparar resultados por:
  - Estado (UF)
  - Sexo
  - Rede de ensino (Pública, Privada e Outros)
- Avaliar o desempenho por área do conhecimento
- Identificar o percentual de estudantes com **alto desempenho (≥ 650 pontos)**  
- Desenvolver um dashboard claro, funcional e adequado para apresentações e portfólio

---

## 🧩 Estrutura do Projeto

```
analise_de_dados_enem_2019/
│
├── dashboard/
│   ├── enem_2019.pbix
│   └── dashboard_preview.png
│
├── scripts/
│   └── tratamento_minimo.py
│
├── README.md
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

1. Download dos microdados do ENEM 2019 (INEP)  
2. Tratamento mínimo dos dados em Python:
   - Seleção de colunas relevantes  
   - Conversão e correção de tipos  
   - Padronização da escala das notas  
3. Geração da base final utilizada no Power BI  
4. Construção das métricas e visualizações utilizando DAX  

---

## 📈 Principais Métricas e Análises

- Total de participantes  
- Média geral do ENEM  
- Média por área do conhecimento:
  - Linguagens
  - Matemática
  - Ciências Humanas
  - Ciências da Natureza
  - Redação
- Média geral por:
  - Estado
  - Sexo
  - Rede de ensino
- Percentual de estudantes com desempenho **≥ 650 pontos**

---

## 🎨 Dashboard

O dashboard foi desenvolvido em **uma única página**, contendo:

- Painel lateral de filtros (Estado, Sexo e Rede de Ensino)
- KPIs principais no topo
- Gráficos comparativos e analíticos
- Layout limpo e orientado à leitura rápida

> 📌 O foco do design foi clareza, organização visual e interpretação educacional dos dados.

*(Adicione aqui a imagem do dashboard, se desejar)*

---

## 📦 Dados

Devido ao tamanho dos arquivos originais, os **microdados do ENEM 2019 não estão versionados neste repositório**, respeitando o limite de upload do GitHub.

Os dados podem ser obtidos diretamente no site oficial do INEP:

🔗 https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados

Após o download, os arquivos devem ser utilizados como entrada para o script de tratamento disponível na pasta `scripts/`.

Essa abordagem segue boas práticas de versionamento e mantém o projeto leve e reprodutível.

---

## ℹ️ Observações

Este projeto foi desenvolvido **integralmente no Power BI Desktop**, por decisão de escopo.

Algumas funcionalidades disponíveis apenas no **Power BI Service** não foram incluídas, mantendo o projeto totalmente funcional em ambiente local, sem dependência de conta institucional ou publicação online.

---

## 📚 Fonte dos Dados

- **INEP – Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira**
- Microdados do ENEM 2019

---

## 👤 Autor

**Antunes Menezes**  
Professor de Matemática | Análise de Dados Educacionais  

Projeto desenvolvido para fins de estudo e portfólio.
