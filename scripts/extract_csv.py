import os
import pandas as pd
from datetime import datetime

# Configurações
CSV_PATH = "data/csv/order_details.csv"
DATE = datetime.now().strftime('%Y-%m-%d')
OUTPUT_DIR = f"data/csv/{DATE}"

# Certificar-se de que o diretório existe
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Carregar CSV e salvar no formato desejado
df = pd.read_csv(CSV_PATH)
df.to_json(f"{OUTPUT_DIR}/order_details.json", orient="records", indent=4)

print(f"Dados CSV exportados para {OUTPUT_DIR}")
