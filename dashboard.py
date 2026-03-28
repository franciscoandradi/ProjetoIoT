import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# Configuração da página
st.set_page_config(page_title="Dashboard IoT", layout="wide")

# Conexão com o banco
DB_USER = "postgres"
DB_PASSWORD = "123456"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "iot_db"

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

def load_data(view_name):
    query = f"SELECT * FROM {view_name}"
    return pd.read_sql(query, engine)

st.title("📊 Dashboard de Temperaturas IoT")

# Gráfico 1
st.header("1. Média de Temperatura por Dispositivo")
df_avg_temp = load_data("avg_temp_por_dispositivo")

fig1 = px.bar(
    df_avg_temp,
    x="device_id",
    y="avg_temp",
    title="Média de Temperatura por Dispositivo"
)
st.plotly_chart(fig1, use_container_width=True)

# Gráfico 2
st.header("2. Leituras por Hora do Dia")
df_leituras_hora = load_data("leituras_por_hora")

fig2 = px.line(
    df_leituras_hora,
    x="hora",
    y="contagem",
    title="Quantidade de Leituras por Hora"
)
st.plotly_chart(fig2, use_container_width=True)

# Gráfico 3
st.header("3. Temperaturas Máximas e Mínimas por Dia")
df_temp_max_min = load_data("temp_max_min_por_dia")

fig3 = px.line(
    df_temp_max_min,
    x="data",
    y=["temp_max", "temp_min"],
    title="Temperaturas Máximas e Mínimas por Dia"
)
st.plotly_chart(fig3, use_container_width=True)