#declarando a variável e recebendo o valor do usuário
numero = float(input("Digite um numero número: "))

#operador ternário para verificar se o número é par ou ímpar
resultado = "par" if numero % 2 == 0 else "ímpar"
print(f"O número é {resultado}.")