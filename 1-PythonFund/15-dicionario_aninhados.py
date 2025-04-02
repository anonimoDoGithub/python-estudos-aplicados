# Inicio do estudo das COLEÇÕES em Python
# Dicionário - dict{}
import pprint 

listaVip = {
    "Pai":{
        "nome": "Mauricio",
        "idade": 84
    },
    
    "Mãe":{
        "nome": "Tereza",
        "idade": 84
    },
    
    "Filha":{
        "nome": "Margarida",
        "idade": 59
    },
    
    "Filho":{
        "nome": "João",
        "idade": 51
    }
    
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(listaVip)

# 1 - Buscar informação dentro de um dicionário aninhado
print(listaVip["Pai"])

# 2 - Adicionar novo item
listaVip["Filha"]["Namorando"] = True
print(listaVip)

# 3 - Excluir um dicionário
del listaVip["Filha"]
pp.pprint(listaVip)