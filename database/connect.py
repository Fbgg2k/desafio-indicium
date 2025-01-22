import psycopg2

def connect_to_db():
    conn = psycopg2.connect(
        dbname="northwind",
        user="admin123",
        password="senha123",
        host="localhost",
        port="5432",
    )
    return conn

def fetch_data():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sua_tabela;")  # Substitua 'sua_tabela' pelo nome da tabela que você deseja consultar
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    conn.close()

if __name__ == "__main__":
    fetch_data()
