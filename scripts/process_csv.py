import pandas as pd
import os

# Caminho do arquivo CSV
csv_file = "data/csv/order_details.csv"

# Ler o arquivo CSV
df = pd.read_csv(csv_file)

# Exibir informações básicas do dataframe
print(f"Linhas: {len(df)}, Colunas: {len(df.columns)}")
print(df.head())

# Criar pasta de saída
output_path = "data/csv/2025-01-22/"
os.makedirs(output_path, exist_ok=True)

# Salvar como parquet
output_file = os.path.join(output_path, "order_details.parquet")
df.to_parquet(output_file, index=False)
print(f"Arquivo salvo em {output_file}")
