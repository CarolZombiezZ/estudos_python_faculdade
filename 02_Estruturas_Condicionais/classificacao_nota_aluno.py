#declarando as variavel e recebendo o valor do usuário
nota = float(input("Digite sua nota: "))

#if para verificar se a nota é maior ou igual a 7, se for, o aluno está aprovado.
# Se a nota for maior ou igual a 5, o aluno está de recuperação. 
# Caso contrário, o aluno está reprovado.
if nota >= 7:
    print("Aprovado")
elif nota >=5:
    print("Recuperação")
else:
    print("Reprovado")