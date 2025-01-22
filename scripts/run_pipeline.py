import os

# Etapas do pipeline
os.system("python scripts/process_csv.py")
os.system("python scripts/extract_postgres.py")
os.system("python scripts/load_to_postgres.py")
