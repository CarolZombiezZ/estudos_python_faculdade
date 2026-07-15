alunos = [
    {"nome": "Ana", "notas": [8, 7, 9]},
    {"nome": "Bruno", "notas": [6, 5, 7]},
    {"nome": "Carlos", "notas": [9, 8, 10]},
    {"nome": "Daniela", "notas": [4, 6, 5]}
]


def calcular_media(notas):
    return sum(notas) / len(notas)


def definir_status(media):

    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"


def analisar_turma(alunos):

    aprovados = 0
    reprovados = 0
    soma_medias = 0

    print("RELATÓRIO DA TURMA")
    print("=" * 40)

    for aluno in alunos:

        try:
            nome = aluno["nome"]
            notas = aluno["notas"]

            media = calcular_media(notas)
            status = definir_status(media)

            soma_medias += media

            if status == "Aprovado":
                aprovados += 1
            else:
                reprovados += 1

            print(f"Aluno: {nome}")
            print(f"Notas: {notas}")
            print(f"Média: {media:.2f}")
            print(f"Status: {status}")
            print("-" * 40)

        except KeyError:
            print("Erro: aluno sem nome ou notas.")

        except ZeroDivisionError:
            print("Erro: divisão por zero.")

        except Exception as erro:
            print(f"Erro inesperado: {erro}")

        finally:
            print("Análise do aluno finalizada.\n")

    media_geral = soma_medias / len(alunos)

    return {
        "media_geral": media_geral,
        "aprovados": aprovados,
        "reprovados": reprovados
    }


resultado = analisar_turma(alunos)

print("RESUMO FINAL")
print("=" * 40)

print(f"Média geral: {resultado['media_geral']:.2f}")
print(f"Aprovados: {resultado['aprovados']}")
print(f"Reprovados: {resultado['reprovados']}")

print("\nALUNOS ORDENADOS")
print("=" * 40)

alunos.sort(key=lambda aluno: aluno["notas"][0])

for aluno in alunos:
    print(f"{aluno['nome']} - Primeira nota: {aluno['notas'][0]}")

print("\nEXEMPLO DE TRATAMENTO DE ERROS")
print("=" * 40)

try:

    numero = int(input("Digite um número: "))

    resultado_divisao = 10 / numero

    print(f"Resultado: {resultado_divisao:.2f}")

except ValueError:

    print("Erro: digite apenas números.")

except ZeroDivisionError:

    print("Erro: não é possível dividir por zero.")

finally:

    print("Programa finalizado.") 