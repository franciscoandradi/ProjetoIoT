import pandas as pd
from sqlalchemy import create_engine, text

# ==============================
# CONFIGURAÇÃO DO BANCO
# ==============================
DB_USER = "postgres"
DB_PASSWORD = "123456"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "iot_db"

# Caminho do CSV
CSV_PATH = "../data/temperature_readings.csv"

# String de conexão (troquei apenas o driver)
DATABASE_URL = f"postgresql+pg8000://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Criando engine
engine = create_engine(DATABASE_URL)

def carregar_csv():
    df = pd.read_csv(CSV_PATH)

    print("Colunas encontradas no CSV:")
    print(df.columns)

    # Renomeando colunas para nomes amigáveis
    df = df.rename(columns={
        "room_id/id": "device_id",
        "noted_date": "timestamp",
        "temp": "temperature",
        "out/in": "location"
    })

    print("\nColunas após renomear:")
    print(df.columns)

    # Converter data
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

    # Remover linhas com data inválida
    df = df.dropna(subset=["timestamp"])

    # Garantir tipo numérico na temperatura
    df["temperature"] = pd.to_numeric(df["temperature"], errors="coerce")
    df = df.dropna(subset=["temperature"])

    return df

def testar_conexao():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        print("✅ Conexão com PostgreSQL OK!")
    except Exception as e:
        print("❌ Erro ao conectar no PostgreSQL:")
        print(e)
        raise

def salvar_no_banco(df):
    df.to_sql("temperature_readings", engine, if_exists="replace", index=False)
    print("✅ Dados inseridos com sucesso na tabela temperature_readings!")

def criar_views():
    with engine.connect() as conn:
        # View 1: média de temperatura por dispositivo
        conn.execute(text("""
            CREATE OR REPLACE VIEW avg_temp_por_dispositivo AS
            SELECT 
                device_id,
                AVG(temperature) AS avg_temp
            FROM temperature_readings
            GROUP BY device_id
            ORDER BY device_id;
        """))

        # View 2: contagem de leituras por hora
        conn.execute(text("""
            CREATE OR REPLACE VIEW leituras_por_hora AS
            SELECT 
                EXTRACT(HOUR FROM timestamp) AS hora,
                COUNT(*) AS contagem
            FROM temperature_readings
            GROUP BY hora
            ORDER BY hora;
        """))

        # View 3: temperaturas máximas e mínimas por dia
        conn.execute(text("""
            CREATE OR REPLACE VIEW temp_max_min_por_dia AS
            SELECT 
                DATE(timestamp) AS data,
                MAX(temperature) AS temp_max,
                MIN(temperature) AS temp_min
            FROM temperature_readings
            GROUP BY data
            ORDER BY data;
        """))

        conn.commit()

    print("✅ Views criadas com sucesso!")

def main():
    print("Iniciando processamento...")

    testar_conexao()

    df = carregar_csv()

    print(f"\nTotal de registros válidos: {len(df)}")

    salvar_no_banco(df)
    criar_views()

    print("\n🎉 Pipeline finalizado com sucesso!")

if __name__ == "__main__":
    main()