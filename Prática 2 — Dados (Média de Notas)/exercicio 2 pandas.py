#Calculando a média com pandas
import pandas as pd

#ler arquivo excel
tabela = pd.read_excel("tarefa_python.xlsx")
#exibir tabela
print(tabela)

#criando coluna média e calculando a média das notas
tabela["média"] = (tabela["Nota 1"] + tabela["Nota 2"]) / 2

# #criando coluna situação e atribuindo a situação de aprovado ou reprovado
tabela.loc[tabela["média"] >=6, "situação"] = "Aprovado"
tabela.loc[tabela["média"] <6, "situação"] = "Reprovado"

# #exibir tabela final atualizada
print("\n--- Resultado Final ---")
print(tabela)