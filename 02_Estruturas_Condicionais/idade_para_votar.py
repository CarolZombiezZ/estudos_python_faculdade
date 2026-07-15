#declarando a variável e recebendo o valor do usuário
idade = int(input("Digite sua idade:"))

#if para verificar se a idade é maior ou igual a 16, se for, 
# o usuário tem idade para votar. 
# Caso contrário, o usuário não pode votar.
if idade >=16:
    print("Você tem idade para votar.")
else:
    print("Você não pode votar")