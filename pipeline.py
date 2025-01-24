import subprocess
import psycopg2
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Caminho dos scripts
SCRIPTS_DIR = "./scripts"

# Configurar conexão com o banco de dados
try:
    conn = psycopg2.connect(
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT")
    )
    print("Conexão com o PostgreSQL estabelecida com sucesso!")
except psycopg2.OperationalError as e:
    print(f"Erro ao conectar ao PostgreSQL: {e}")
    exit()

# Executar etapas
print("1. Extraindo dados do PostgreSQL...")
subprocess.run(["python", f"{SCRIPTS_DIR}/extract_postgres.py"])

print("2. Extraindo dados do CSV...")
subprocess.run(["python", f"{SCRIPTS_DIR}/extract_csv.py"])

print("3. Carregando dados no PostgreSQL...")
subprocess.run(["python", f"{SCRIPTS_DIR}/load_to_postgres.py"])

conn = psycopg2.connect(
    database="northwind",
    user="postgres",  # Verifique se o usuário é correto
    password="123456",  # Senha correta
    host="localhost",  # Host corrigido
    port="5432"
)