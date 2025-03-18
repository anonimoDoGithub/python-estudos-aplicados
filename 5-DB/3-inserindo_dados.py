import sqlite3

# 1 - Conectando ao BD
connection = sqlite3.connect("title.db") # No caso do Banco de Dados já criado ele CONECTA com o Banco de Dados.

# 2 - Criando um Cursor
'''
Cursor é um interador que permite navegar e manipular os registros em um Banco de Dados
'''
cursor = connection.cursor()