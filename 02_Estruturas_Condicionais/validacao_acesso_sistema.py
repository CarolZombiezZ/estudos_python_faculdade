#declarando as variaveis e recebendo valores do usuárioS
usuario = input("Digite seu nome de usuário:")
senha = input("Digite sua senha:")

#if para validar o acesso ao sistema, 
# verificando se o nome de usuário é "admin" e a senha é "1234". 
# Se ambos forem verdadeiros, o acesso é permitido. 
# Caso contrário, o acesso é negado.

if usuario == "admin" and senha == "1234":
    print("Acesso permitido.")
else:
    print("Acesso negado")