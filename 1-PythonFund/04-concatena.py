name = input("Digite o nome do jogo: \n")
yearLaunch = int(input("Digite o ano do jogo: \n"))
gamePrice = float(input("Digite o valor do jogo R$: \n"))
planIncluded = input("O jogo está incluso no plano? \n")

print("### Dados do Jogo ###")

# Alternativa 1
'''
print("Nome do Jogo: ", name)
print("Ano de Lançamento: ", yearLaunch)
print("Preço do Jogo: R$", gamePrice)
print("Incluso no Plano: ", planIncluded)
'''

# Alternativa 2 - F STRING Formatação de String (Recomendado)
print(f"Nome do Jogo: {name}")
print(f"Ano de Lançamento: {yearLaunch}")
print(f"Preço do Jogo: R${gamePrice}")
print(f"Incluso no Plano: {planIncluded}")