"""
Substituindo Caracteres Repetido:
-> Escreva um programa Python para obter uma String de uma determinada String
em que todas as ocorrências de seu primeiro caractere foram alteradas para '$'
exceto o próprio primeiro caractere.
Ex: fifa 23 -> fi$a 23
"""
name = input("Digite o nome do jogo: \n")

char = name[0].lower()
new_name = name.replace(char, '$')
new_name = char + new_name[1:]

print(new_name)


""" 
Troca de Caracteres:
-> Escreva um programa Python para obter uma única string de duas strings fornecidas,
separadas por um espaço e troque os dois primeiros caracteres de cada string.
Ex: abc xyz -> xyc abz
"""
st1 = 'abc'
st2 = 'xyz'

new_st1 = st2[:2] + st1[2:]
new_st2 = st1[:2] + st2[2:]
print(new_st1)
print(new_st2)
