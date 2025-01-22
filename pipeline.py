import subprocess

# Caminho dos scripts
SCRIPTS_DIR = "./scripts"

# Executar etapas
print("1. Extraindo dados do PostgreSQL...")
subprocess.run(["python", f"{SCRIPTS_DIR}/extract_postgres.py"])

print("2. Extraindo dados do CSV...")
subprocess.run(["python", f"{SCRIPTS_DIR}/extract_csv.py"])

print("3. Carregando dados no PostgreSQL...")
subprocess.run(["python", f"{SCRIPTS_DIR}/load_to_postgres.py"])
