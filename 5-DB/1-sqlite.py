import sqlite3

# 1 - Criando o DB - Banco de Dados
connection = sqlite3.connect("title.db")

# 2 - Verifica se houve alterações na Base de Dados
print(f"Número de alterações na Base de Dados: {connection.total_changes}")