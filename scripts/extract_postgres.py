import psycopg2
import os
import json
from datetime import datetime

# Configurações de conexão
HOST = "localhost"
DATABASE = "northwind"
USER = "postgres"
PASSWORD = "123456"

# Tabelas para extrair
TABLES = ["categories", "customers", "employees", "orders", "products", "regions", "shippers", "suppliers", "territories"]

# Diretório base
DATE = datetime.now().strftime('%Y-%m-%d')
BASE_DIR = f"data/postgres"

# Função para exportar dados
def export_table(table_name):
    try:
        # Conexão ao banco
        conn = psycopg2.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()

        # Pegando cabeçalhos das colunas
        col_names = [desc[0] for desc in cursor.description]
        data = [dict(zip(col_names, row)) for row in rows]

        # Salvar os dados localmente
        table_dir = os.path.join(BASE_DIR, table_name, DATE)
        os.makedirs(table_dir, exist_ok=True)
        with open(f"{table_dir}/data.json", "w") as f:
            json.dump(data, f, indent=4)
        
        print(f"Dados exportados para {table_name}")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Erro ao exportar {table_name}: {e}")

# Loop nas tabelas
for table in TABLES:
    export_table(table)
