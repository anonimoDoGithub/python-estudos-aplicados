print("Lista de Convidados \n")
name = print("Digite o nome que deseja adicionar: \n")

"""
Arquivos:
1 - opção w - write
2 - opção a - append
3 - opção r - read
"""
file = open("convidados.txt", "w") #abrindo arquivo com o metodo open("colocando o nome do arquivo", "colocando o modo: w, a ou r")
file.write(name)
file.close() #fechando o arquivo, sempre lembrar de fechar o arquivo com close()