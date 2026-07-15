# Importa a biblioteca para gráficos e dá a ela o "apelido" de plt
import matplotlib.pyplot as plt

# Dados de exemplo / Define os dados que vão aparecer no gráfico
meses = ["Jan", "Fev", "Mar", "Abr", "Mai"]
vendas = [100, 150, 130, 170, 200]

# Cria o gráfico de linha / O comando 'plt.plot' cria o gráfico de LINHA ligando os pontos (meses e vendas)
plt.plot(meses, vendas)

#Adiciona textos para deixar o gráfico informativo
# Título do gráfico
plt.title("Vendas por mês")
# Nome do eixo X
plt.xlabel("Meses")
# Nome do eixo Y
plt.ylabel("Vendas")

# Exibe o gráfico / Abre uma janela para mostrar o gráfico finalizado
plt.show()