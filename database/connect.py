import psycopg2

def connect_to_db():
    conn = psycopg2.connect(
        dbname="northwind",
        user="admin",
        password="senha123",
        host="localhost",
        port="5432",
    )
    return conn

def fetch_all_data():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sua_tabela;")  # Substitua 'sua_tabela'
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    conn.close()

def fetch_table_data(table_name):
    conn = connect_to_db()
    cursor = conn.cursor()
    query = f"SELECT * FROM {table_name};"
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)
    except Exception as e:
        print(f"Erro ao consultar a tabela {table_name}: {e}")
    finally:
        cursor.close()
        conn.close()
