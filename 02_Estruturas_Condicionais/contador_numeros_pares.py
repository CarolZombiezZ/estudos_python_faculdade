# Lista de números
numeros = [1, 4, 7, 10, 13, 16, 20]

# Contador de números pares / O contador começa em 0 e vai aumentando cada vez que 
# encontramos um número par
contador = 0

# Percorre cada número da lista / O comando 'for' vai repetir o bloco de código abaixo 
# para cada número da lista 'numeros'
for numero in numeros:
    
    # Verifica se o número é par / O comando 'if' verifica se a condição é verdadeira 
    # (número dividido por 2 tem resto 0)
    if numero % 2 == 0:
        
        # Se for par, soma 1 no contador / O comando 'contador = contador + 1' é a mesma coisa que 
        # 'contador += 1', ou seja, aumenta o valor do contador em 1
        contador = contador + 1

# Mostra quantos números pares existem na lista / O comando 'print' exibe a mensagem e o valor do contador na tela
print("Quantidade de números pares:", contador)