import mysql.connector

def create_connection():
    """Cria uma nova conexão com o banco de dados MySQL."""
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234',
        database='HomeIOT'
    )

def close_connection(connection):
    """Fecha a conexão com o banco de dados."""
    if connection.is_connected():
        connection.close()