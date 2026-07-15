# 1. Importações
import math

# 2. Definição da função com tratamento de erro
def calcular_raiz(numero):
    try:
        resultado = math.sqrt(numero)
        return resultado
    except ValueError:
        return "Erro: Não é possível calcular a raiz de um número negativo!"

# 3. Função principal e execução
def main():
    numero_usuario = 16
    resposta = calcular_raiz(numero_usuario)
    
    # 4. Print para mostrar no terminal
    print(f"O resultado é: {resposta}")

# Executa o programa
if __name__ == "__main__":
    main()