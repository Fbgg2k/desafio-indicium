from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def extract_postgres():
    # Código para extrair dados do PostgreSQL
    pass

def extract_csv():
    # Código para processar dados do CSV
    pass

with DAG(
    "data_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval="0 1 * * *",
) as dag:
    task1 = PythonOperator(
        task_id="extract_postgres",
        python_callable=extract_postgres,
    )
    task2 = PythonOperator(
        task_id="extract_csv",
        python_callable=extract_csv,
    )
    task1 >> task2
