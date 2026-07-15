#declarando as variáveis e recebendo os valores do usuário

numero = float(input("Digite um numero: "))

#if para verificar se o número é positivo, negativo ou zero.
#elif serve para verificar se o número é negativo, caso contrário,
# o número é zero.
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo")
else:
    print("O número é zero.")