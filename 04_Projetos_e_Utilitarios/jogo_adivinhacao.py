# Jogo de Adivinhação em Python
# import da biblioteca random para gerar números aleatórios
import random

# Exibe uma mensagem de boas-vindas e instruções para o jogador
# O comando 'print' é usado para mostrar mensagens na tela. 

print("=" * 50)
print("🎯 BEM-VINDO AO JOGO DE ADIVINHAÇÃO EM PYTHON 🎯")
print("=" * 50)

# Escolha do nível 
print("\nEscolha o nível de dificuldade:")
print("1 - Fácil   (número entre 1 e 10)")
print("2 - Médio   (número entre 1 e 50)")
print("3 - Difícil (número entre 1 e 100)")

# O comando 'input' exibe uma mensagem e espera o usuário digitar algo, que é armazenado na variável 
# 'nivel'
nivel = input("Digite o nível desejado (1, 2 ou 3): ")

# Define o limite do número secreto e a quantidade de tentativas com base no nível escolhido
# O comando 'if' é usado para tomar decisões no código, ou seja, executar um bloco de código 
# diferente dependendo da condição (neste caso, o nível escolhido)
#
if nivel == "1":
    limite = 10
    tentativas = 5

# O comando 'elif' é a abreviação de 'else if' e é usado para verificar outra condição se 
# a primeira condição do 'if' for falsa. Ele permite criar múltiplas condições para o código
elif nivel == "2":
    limite = 50
    tentativas = 7
elif nivel == "3":
    limite = 100
    tentativas = 10

# O comando 'else' é usado para definir um bloco de código que será executado se todas as 
# condições anteriores (do 'if' e 'elif') forem falsas.
#  Ele é opcional, mas é útil para lidar com casos em que o usuário digita algo diferente do esperado
else:
    print("\nOpção inválida. O jogo será iniciado no modo Fácil.")
    limite = 10
    tentativas = 5

# Gera um número secreto aleatório entre 1 e o limite definido para o nível escolhido
numero_secreto = random.randint(1, limite)
pontos = 100

# Exibe uma mensagem informando o jogador sobre o número secreto e as tentativas disponíveis
print(f"\n✅ O computador escolheu um número entre 1 e {limite}.")
print(f"Você tem {tentativas} tentativas para acertar!\n")

# Laço para as tentativas do jogador / O comando 'for' vai repetir o bloco de código abaixo 
# 'tentativas' vezes,e a variável 'rodada' vai receber o número da tentativa atual (começando em 1)
for rodada in range(1, tentativas + 1):
    print(f"--- Tentativa {rodada} de {tentativas} ---")

    palpite_texto = input("Digite seu palpite: ")

    # Verificação para evitar erro caso o usuário digite texto
    if not palpite_texto.isdigit():
        print("⚠️ Você deve digitar apenas números inteiros.\n")
        continue

    palpite = int(palpite_texto)

    # Verifica se o palpite está dentro do limite permitido / O comando 'if' verifica se o palpite 
    # é menor que 1 ou maior que o limite definido para o nível escolhido
    if palpite < 1 or palpite > limite:
        print(f"⚠️ Digite um número entre 1 e {limite}.\n")
        continue

    # Verifica se o palpite é igual ao número secreto / O comando 'if' verifica se o palpite
    #  do jogador é igual ao número secreto gerado pelo computador
    if palpite == numero_secreto:
        print(f"\n🎉 Parabéns! Você acertou o número secreto: {numero_secreto}")
        print(f"🏆 Sua pontuação final foi: {pontos} pontos")
        # O comando 'break' é usado para sair imediatamente do laço 'for', ou seja, 
        # parar de repetir o bloco de código
        break
    else:
        diferenca = abs(numero_secreto - palpite)
        pontos -= diferenca

        if palpite < numero_secreto:
            print("📉 O número secreto é MAIOR que o seu palpite.")
        else:
            print("📈 O número secreto é MENOR que o seu palpite.")

        # Dica extra
        if diferenca <= 3:
            print("🔥 Você está muito perto!")
        elif diferenca <= 10:
            print("🙂 Está chegando...")
        else:
            print("❄️ Ainda está longe...")

        print(f"⭐ Pontuação atual: {pontos}\n")

else:
    print("\n😢 Suas tentativas acabaram!")
    print(f"O número secreto era: {numero_secreto}")
    print(f"Sua pontuação final foi: {pontos}")
    
print("\nObrigado por jogar!")
print("=" * 50)