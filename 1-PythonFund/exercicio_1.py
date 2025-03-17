'''
Escreva um programa em Python que leia um número 
e represente o número ANTECESSOR e SUCESSOR desse número que foi lido,
utilizando operadores de ATRIBUIÇÃO.
'''
print("### ANTECESSOR e SUCESSOR ###")

numero_escolhido = int(input("Digite um número: "))
antecessor = numero_escolhido - 1
sucessor = numero_escolhido + 1
print(f"O número escolhido foi {numero_escolhido}, seu ANTECESSOR é {antecessor} e o seu SUCESSOR é {sucessor}")

'''
Escreva um programa em Python que leia 4 NÚMEROS e calcule a MÉDIA entre eles .
'''
print("### MÉDIA DE 4 NOTAS ###")

av1 = int(input("Digite AV1: \n"))
av2 = int(input("Digite AV2: \n"))
av3 = int(input("Digite AV3: \n"))
av4 = int(input("Digite AV4: \n"))

soma = av1 + av2 + av3 + av4
media = soma / 4

print(f"A média das notas é: {media}")