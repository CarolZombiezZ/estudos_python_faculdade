#declarando variáveis e recebendo os valores do usuário
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))
nota4 = float(input("Digite sua quarta nota: "))

frequencia = float(input("Digite sua frequência: "))


#calculando a média 
media = (nota1 + nota2 + nota3 + nota4) / 4

#if para verificar se as notas e a frequência estão dentro dos valores válidos, 
# caso contrário, o programa informa que os valores são inválidos.
if (nota1 < 0 or nota1 > 10) or (frequencia < 0 or frequencia > 100):
    print("Valor inválido. As notas devem estar entre 0 e 10, e a frequência entre 0 e 100.")

#else para verificar se a média é maior ou igual a 7 e a frequência é maior ou igual a 75, 
# caso contrário, o programa informa que o aluno está reprovado.
else:
    media = (nota1 + nota2 + nota3 + nota4) / 4

    if media >= 7 and frequencia >= 75:
        print(f"Média: {media} | Frequência: {frequencia}%")
        print("Parabéns, você foi aprovado!")
    else:
        print(f"\n\n❌ RETIDO")
        if media < 7 and frequencia < 75:
            print(f"Motivo: Média baixa ({media:.1f}) e faltas excessivas ({frequencia}%).")
        elif media < 7:
            print(f"Motivo: Sua média foi {media:.1f} (mínimo exigido: 7.0).")
        else:
            print(f"Motivo: Sua frequência foi {frequencia}% (mínimo exigido: 75%).")