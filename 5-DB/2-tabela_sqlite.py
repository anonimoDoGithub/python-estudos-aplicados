import sqlite3

# 1 - Conectando ao BD
connection = sqlite3.connect("title.db") # No caso do Banco de Dados já criado ele CONECTA com o Banco de Dados.

# 2 - Criando um Cursor
'''
Cursor é um interador que permite navegar e manipular os registros em um Banco de Dados
'''
cursor = connection.cursor()

# 3 - Criando a Tabela
cursor.execute("""
    CREATE TABLE movies(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        year INTEGER NOT NULL,
        score REAL NOT NULL
    );
                """)
# CREATE TABLE Criar Tabela - movies -> Nome da Tabela
# id Campo da Tabela
# INTEGER Tipo INTEIRO
# TEXT Tipo CARACTER
# REAL Tipo DECIMAL
# NOT NULL O campo NÃO PODE FICAR VÁZIO
# PRIMARY KEY Chave Primaria
# AUTOINCREMENT Será ingrementado automaticamente

# 4 - Fechando a Conexão
print("Tabela criada com sucesso!")
connection.close()
