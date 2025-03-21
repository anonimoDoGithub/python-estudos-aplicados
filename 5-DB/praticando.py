import sqlite3

connection = sqlite3.connect("meu_bando_de_dados.db")

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE meu_dados (
               id       SERIAL      NOT NULL,
               nome     VARCHAR(60) NOT NULL,
               cpf      INTEGER     NOT NULL,
               telefone INTEGER     NOT NULL
               );
                """)

cursor.close()
print("Tabela criada com sucesso!")