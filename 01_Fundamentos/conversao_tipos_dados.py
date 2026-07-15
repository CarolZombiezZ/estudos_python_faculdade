# Este programa solicita ao usuário que digite um número inteiro, um número de ponto flutuante e um valor booleano, e depois exibe os valores digitados.
numero1 = int(input("Digite um numero inteiro: "))
numero2 = float(input("Digite um numero de ponto flutuante: "))
valor_booleano = input("Digite um valor booleano (True ou False): ")

valor_booleano = valor_booleano.lower()  # Converte para minúsculas para garantir que seja reconhecido como booleano
valor_booleano = valor_booleano == "true"  # Converte para tipo bool

print("O numero inteiro digitado foi:", numero1)
print("O numero de ponto flutuante digitado foi:", numero2)
print("O valor booleano digitado foi:", valor_booleano)