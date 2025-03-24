gameDescription = """
    Fifa 23 é um jogo bom!
    Um jogo de futebol!
""" # String multilinha

gameName = "Fifa23"
numeros = "0123456789"

# SLICE string[início:fim] - índice começa na posição 0 | índice final -1

# 1 - Busque toda string a partir da primeira posição
print(gameName[0:])

# 2-- Busque toda string até a última posição
print(gameName[:7])

# 3 - Busque toda string da terceira até a última posição
print(gameName[2:])

"""
string[início:fim:passo] - Índice começa na posição 0 | índice final -1
passo - Determina o incremento. Por padrão esse número é o 1.
"""
# 4 - Busque toda string de 2 em 2 caracteres
print(numeros[::2])

# 5 - Busque toda string nos índices ímpares
print(numeros[1::2])