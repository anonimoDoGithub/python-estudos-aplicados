# Inicio do estudo das COLEÇÕES em Python
# Dicionário - dict{}

convidado = {
    "nome": "Maria",
    "idade": 23,
    "genero": "cisgênero",
    "contato": 9999999,
    "email": "ma@email.com"
}
print(convidado)
print(len(convidado))
print(type(convidado))

# 1 - Recuperar um elemento do dicionário
print(convidado.get('nome'))
print(convidado['idade'])

# 2 - Buscar apenas as chaves do dicionário
print(convidado.keys())

# 3 - Buscar apenas os valores do dicionário
print(convidado.values())

# 4 - Buscar itens do dicionário com chave e valor
print(convidado.items())

# 5 - Adicionar itens no dicionário
convidado["altura"] = 1.85
print(convidado)

# 6 - Atualizar itens no dicionário
convidado.update({"altura": 1.80})
print(convidado)

# 7 - Remover itens no dicionário
convidado.pop('altura')
print(convidado)