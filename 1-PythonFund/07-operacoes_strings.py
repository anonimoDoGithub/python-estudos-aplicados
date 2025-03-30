gameDescription = """
    Fifa 23 é um jogo bom!
    Um jogo de futebol!
""" # String multilinha

gameName = "Fifa"
gameVersion = "23"
line = "#"
palavra = input("Digite a palavra que deseja encontrar: ")

# 1 - Concatenação de Strings
gameFullName = gameName + gameVersion
print(gameFullName)

# 2 - Operação de Multiplicação de Strings
print(line * 25)

# 3 - Procurando palavras dentro de um texto => Usando in
if palavra in gameDescription:
    print("Palavra encontrada!")
else:
    print("Palavra não encontrada")
