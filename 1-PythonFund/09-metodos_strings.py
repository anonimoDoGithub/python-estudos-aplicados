gameDescription = """
    Fifa 23 é um jogo bom!
    Um jogo de futebol!
""" # String multilinha

gameName = "Fifa23"

user1 = "maria"
user2 = "joão"
address = "Avenida Santo,56,Brazil,+5599999-9999"

position = "centralizado"

print(gameDescription.upper()) # Retorna string em maísculo
print(gameDescription.lower()) # Retorna string em minúsculo
print(f"{user1.capitalize()} e {user2.title()}") # Apenas a primeira letra em maiúsculo
print(position.center(16, '-')) # Retorna a string centralizada com caractere de preenchimento
print(user1.find("i")) # Retorna a posição de um determinado caractere
print(gameDescription.count("o")) # Conta caracteres
print(f"Usuário {user1}, agora é {user1.replace(user1, user2)}")
print(address.split(f"{','}"))