#declarando as variáveis e recebendo os valores do usuário
valor1 = float(input("Digite um número:"))
valor2 = float(input("Digite outro número:"))

#if para verificar qual número é maior, se os números forem iguais,
# o programa informa que os números são iguais.
if valor1 > valor2:
    print("O maior número é: ", valor1)
elif valor1 == valor2:
    print("Os números são iguais.")
else:
    print("O maior número é: ", valor2)