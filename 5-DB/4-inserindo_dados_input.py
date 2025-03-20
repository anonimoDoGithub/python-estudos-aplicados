import sqlite3

# 1 - Conectando ao BD
connection = sqlite3.connect("title.db") # No caso do Banco de Dados já criado ele CONECTA com o Banco de Dados.

# 2 - Criando um Cursor
'''
Cursor é um interador que permite navegar e manipular os registros em um Banco de Dados
'''
cursor = connection.cursor()

# 3 - Solicitando Dados do Usuário
name = input("Nome do Filme \n")
year = int(input("Ano do Filme \n"))
score = float(input("Nota do Filme \n"))

# 4 - Inserindo Dados
cursor.execute("""
    INSERT INTO movies (name, year, score)
    VALUES  (?, ?, ?)
                """, (name, year, score))


# 4 - Gravando Dados no BD
connection.commit()
print("Dados inseritos com sucesso!")

# 5 - Fechando conexào
connection.close()