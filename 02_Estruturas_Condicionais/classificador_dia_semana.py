#declarando variaveis e recebendo valores do usuário
dia = input("Digite o dia da semana: ")

#if para verificar se o dia é um dia útil ou um fim de semana

#dia.lower() é usado para converter a entrada do usuário para minúsculas,
#garantindo que a comparação seja feita de forma consistente, independentemente de como o usuário digite o dia da semana.
if dia.lower() in ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"]:
    print("É um dia útil.")
elif dia.lower() in ["sábado", "domingo"]:
    print("É um fim de semana.")