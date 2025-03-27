# Inicio do estudo das COLEÇÕES em Python
# Em uma LISTA Podemos armazenar dados HETEROGÊNEOS["Fifa 23", 2025, 10.0, True] Ex: 'String', int, float, bolean

listaConvidados = ["Zeca", "Ana", "Margarida", "João", "Mauro", "Juliana", "Maria", "Jorge", "Antônia", "Ricardo", "Joana"]
print(listaConvidados)

# 1 - len() Tamanho da lista
print(f"Número de convidados na lista: {len(listaConvidados)} convidados.")

# 2 - index() Recuperar um item da lista pelo índice
buscarConvidado = input("Digite o nome do convidado: ")
convidadoEncontrado = listaConvidados.index(buscarConvidado)
print(f"Convidado(a), {buscarConvidado} encontrado, número {convidadoEncontrado} na lista.")

# 3 - append() Adicionar item ao final da lista
adicionarConvidado = input("Informe o convidado que deseja adicionar: ")
convidadoAdicionado = listaConvidados.append(adicionarConvidado)
print(f"Convidado(a) {adicionarConvidado}, adicionado a lista!")

# 4 - sort() Ordenar a lista
listaAtualizada = listaConvidados.sort()
print(f"Convidados listados: {listaConvidados}")

# 5 - copy() Copia os itens de uma lista para outra
listaVip = listaConvidados.copy()

# 6 - remove() Remove um item da lista
listaVip.remove("Ana")
print(listaVip)

# 7 - clear() Remover todos os itens da lista
listaConvidados.clear()
print(f"Todos os convidados da lista removidos!")