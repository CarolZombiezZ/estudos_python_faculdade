import matplotlib.pyplot as plt
import numpy as np

# Dados de exemplo
disciplinas = ["Cálculo", "POO", "BD", "Redes", "IA"]
medias = [6.8, 8.2, 7.5, 7.0, 8.9]
cores = ["#e74c3c", "#2ecc71", "#3498db", "#f39c12", "#9b59b6"]

# Gráfico de barras
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Gráfico 1: Barras por disciplina
axes[0].bar(disciplinas, medias, color=cores)
axes[0].set_title("Média por Disciplina")
axes[0].set_ylabel("Nota média")
axes[0].set_ylim(0, 10)

# Gráfico 2: Pizza de aprovação
reprovados = [d for d, m in zip(disciplinas, medias) if m < 7]
aprovados_n = sum(1 for m in medias if m >= 7)
reprovados_n = len(medias) - aprovados_n

axes[1].pie([aprovados_n, reprovados_n], 
            labels=["Aprovados", "Reprovados"],
            autopct="%1.0f%%", colors=["#2ecc71", "#e74c3c"])
axes[1].set_title("Situação Geral")

plt.tight_layout()
plt.savefig("relatorio_notas.png")
plt.show()

#esse código é um exemplo de como usar a biblioteca Matplotlib para criar gráficos de barras e pizza a partir de dados de notas médias por disciplina. 
# Ele também salva o gráfico como uma imagem PNG.