# Quantidade de números da sequência que queremos gerar
n = 10

# Primeiros valores da sequência
a = 0
b = 1

# Exibe mensagem inicial
print("Sequência de Fibonacci:")

# Laço para gerar a sequência / O comando 'for' vai repetir o bloco de código abaixo 'n' vezes
for i in range(n):
    
    # Mostra o número atual da sequência
    print(a)
    
    # Calcula o próximo número da sequência / O próximo número é a soma dos dois anteriores
    proximo = a + b
    
    # Atualiza os valores de 'a' e 'b' para a próxima iteração / E o 'b' recebe o novo valor calculado (a soma)
    a = b
    b = proximo