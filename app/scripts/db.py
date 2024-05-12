import os
import sqlite3

def db(query, parameters=()):
    # Obter o caminho do banco de dados
    db_path = os.path.join(os.path.dirname(__file__), "..", "data", "database.db")
    
    # Conectar-se ao banco de dados e executar a consulta
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(query, parameters)
        result = cursor.fetchall()  # Use fetchall() para recuperar todos os registros, se houver
        conn.commit()
        return result
