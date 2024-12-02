import sqlite3

def create_database():
    # Conecta ao banco de dados (ou cria, se não existir)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Criação da tabela de usuários
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    ''')
    
    # Insere um usuário inicial (opcional, para testes)
    cursor.execute('''
    INSERT OR IGNORE INTO users (username, password)
    VALUES ('admin', 'admin123')
    ''')
    
    # Salva as alterações e fecha a conexão
    conn.commit()
    conn.close()
    print("Banco de dados criado com sucesso.")

if __name__ == "__main__":
    create_database()
