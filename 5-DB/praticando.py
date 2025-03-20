import sqlite3

connection = sqlite3.connect("meu_db.db")

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE clientes(
                id          SERIAL,
                nome        VARCHAR(30) NOT NULL,
                telefone    INTEGER     NOT NULL,
                email       VARCHAR(30) NOT NULL,
                observacoes TEXT
                            );
                """)

print("Tabela criado com sucesso!")
cursor.close()