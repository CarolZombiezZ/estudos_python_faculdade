import numpy as np

# Criando arrays
notas = np.array([7.5, 8.0, 6.5, 9.0, 5.5, 8.5, 7.0])

# Estatísticas básicas
print(f"Média: {np.mean(notas):.2f}")          # 7.43
print(f"Mediana: {np.median(notas):.2f}")      # 7.50
print(f"Desvio padrão: {np.std(notas):.2f}")   # 1.10
print(f"Maior nota: {np.max(notas)}")          # 9.0

# Operações vetorizadas (sem loop!)
notas_dobradas = notas * 2
notas_normalizadas = (notas - np.min(notas)) / (np.max(notas) - np.min(notas))
print(notas_normalizadas)

# Álgebra linear (muito usada em ML)
matriz_A = np.array([[1, 2], [3, 4]])
matriz_B = np.array([[5, 6], [7, 8]])

produto = np.dot(matriz_A, matriz_B)
print(produto)
# [[19 22]
#  [43 50]]

#esse código é um exemplo de como usar a biblioteca NumPy para manipular arrays e realizar operações matemáticas.