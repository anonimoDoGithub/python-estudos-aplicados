print("Lista de Convidados \n")
convidados = input("Digite o nome que deseja adicionar: \n")

"""
Arquivos:
1 - opção w - write
2 - opção a - append
3 - opção r - read
"""
#abrindo arquivo com o metodo open("colocando o nome do arquivo", "colocando o modo: w, a ou r")
#file = open("convidados.txt", "w") #como não tem nenhum arquivo ainda criado, precisamos criar primeiro usando o "w"
file = open("convidados.txt", "a") #logo em seguida para adicionar nomes usamos o "a"
file.write(f"{convidados} \n") #usando o F para formatar a string, colocando uma quebra de linha com o \n
file.close() #fechando o arquivo, sempre lembrar de fechar o arquivo com close()