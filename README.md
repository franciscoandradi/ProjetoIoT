#  Pipeline de Dados IoT com PostgreSQL e Streamlit

##  Sobre o Projeto

Este projeto tem como objetivo simular um **pipeline de dados aplicado ao contexto de Internet das Coisas (IoT)**, utilizando leituras de temperatura coletadas por sensores em diferentes ambientes.

A proposta consiste em demonstrar, na prática, como dados de sensores podem ser:

- carregados a partir de um arquivo CSV;
- tratados e validados com Python;
- armazenados em um banco de dados PostgreSQL;
- organizados por meio de **views SQL**;
- visualizados em um **dashboard interativo com Streamlit**.

Esse fluxo representa uma solução simples, mas bastante próxima de cenários reais de monitoramento e análise em ambientes IoT.

---

##  Tecnologias Utilizadas

- **Python 3**
- **Pandas**
- **SQLAlchemy**
- **pg8000**
- **PostgreSQL**
- **Docker / Docker Compose**
- **Streamlit**
- **Plotly**
- **GitHub**

---

<img width="1915" height="872" alt="views" src="https://github.com/user-attachments/assets/9dfdbf92-5d65-4e45-9e71-de384e764319" />
Assim ficará

---
##  Estrutura do Projeto

```bash
PIPELINE-IOT-TEMPERATURA/
│
├── data/
│   └── temperature_readings.csv  
│
├── sql/
│   └── views.sql
│
├── src/
│   ├── main.py
│   ├── dashboard.py
│  
│
├── .gitignore
├── README.md
└── requirements.txt
