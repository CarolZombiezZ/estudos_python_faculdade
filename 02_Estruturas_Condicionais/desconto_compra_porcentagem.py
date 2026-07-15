#declarando as variáveis e recebendo os valores do usuário
valor = float(input("Digite o valor da compra: R$"))

#verifica se o valor é maior que 100
if valor > 100:
    valor_final = valor * 0.9
    print(f"Sua compra é elegível para desconto. O valor final com desconto é: R$ {valor_final:.2f}")
else:
    print(f"O valor da compra não é elegível para desconto. Valor final da compra: R$ {valor:.2f}")
#f string para formatar o valor final com duas casas decimais.