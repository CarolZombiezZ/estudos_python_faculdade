# Função que calcula a área de um retângulo / O comando 'def' é usado para criar uma função, ou seja, 
# um bloco de código que pode ser reutilizado várias vezes
def calcular_area(base, altura):
    
    # Multiplica base pela altura
    area = base * altura
    
    # Retorna o valor calculado
    return area


# Solicita valores ao usuário / O comando 'input' exibe uma mensagem e espera o usuário digitar algo, 
# que é armazenado na variável
base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))

# Chama a função criada e armazena o resultado na variável 'resultado' / 
# O comando 'calcular_area(base, altura)' executa a função com os valores fornecidos
resultado = calcular_area(base, altura)

# Exibe o resultado
print("A área do retângulo é:", resultado)