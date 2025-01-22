import psycopg2
import os
import json

# Configurações de conexão
HOST = "localhost"
DATABASE = "northwind"
USER = "postgres"
PASSWORD = "123456"

# Tabelas para carregar
TABLES = ["categories", "customers", "employees", "orders", "products", "regions", "shippers", "suppliers", "territories"]

# Caminho dos dados exportados
DATE = "2025-01-22"  # Trocar pela data desejada
BASE_DIR = f"data/postgres"

# Função para importar dados
def load_table(table_name):
    try:
        # Conexão ao banco
        conn = psycopg2.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
        cursor = conn.cursor()

        # Carregar dados do arquivo
        file_path = os.path.join(BASE_DIR, table_name, DATE, "data.json")
        with open(file_path, "r") as f:
            data = json.load(f)

        # Inserir dados no PostgreSQL
        for row in data:
            columns = ", ".join(row.keys())
            values = ", ".join([f"%({x})s" for x in row.keys()])
            query = f"INSERT INTO {table_name} ({columns}) VALUES ({values}) ON CONFLICT DO NOTHING;"
            cursor.execute(query, row)

        conn.commit()
        cursor.close()
        conn.close()
        print(f"Tabela {table_name} carregada com sucesso.")
    except Exception as e:
        print(f"Erro ao carregar {table_name}: {e}")

# Loop nas tabelas
for table in TABLES:
    load_table(table)
