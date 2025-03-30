# Inicio do estudo das COLEÇÕES em Python
# tuplas()

listaConvidados = ("Zeca", "Ana", "Margarida", "João", "Mauro", "Juliana", "Maria")
print(listaConvidados)
print(type(listaConvidados))

# Limitações de um tupla()
# Não possibilida adicionar valores na tupla
# Não possibilida remover valores na tupla
# Não possibilida ordenar valores na tupla

#Obs: Não é permitido repetir valores!

# Buscar informação atravez do SLICE() FATIAMENTO

# 1 - Buscar os dois primeiros itens da tupla
print(listaConvidados[:2])

# 2 - Buscar o último item da tupla
print(listaConvidados[-1])

# 3 - Buscar até uma determinada posição
print(listaConvidados[1:4])

# 4 - Buscar de uma posição em diante
print(listaConvidados[2:])

# 5 - Recuperar um item da tupla pelo índice - .index()
print(listaConvidados.index("Mauro"))