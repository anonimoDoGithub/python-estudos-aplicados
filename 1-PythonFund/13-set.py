# Inicio do estudo das COLEÇÕES em Python
# set{}

listaConvidados = {"Zeca", "Ana", "Margarida", "João", "Mauro", "Juliana", "Maria"}
listaVip = {"Marcos", "Marcia", "Mauricio"}

# Limitações de um set{}
# Não possibilida recuperar valores via FATIAMENTO ou SLICE
# Não possibilida remover valores na tupla
# Não possibilida ordenar valores na tupla

""" 
Obs: 
True e 1, são considerados o mesmo valor. 
Não é permitido repetir valores!
"""

# 1 - Buscar o tamanho do set{}
print(len(listaConvidados))

# 2 - Adicionar item de outro set{}
listaConvidados.update(listaVip)
print(listaConvidados)

# 3 - Remover um item do set{}
listaVip.remove("Marcos")
print(listaVip)