import pandas as pd

# Carregando um CSV de notas de alunos
df = pd.read_csv("notas_alunos.csv")

# Visualizando as primeiras linhas
print(df.head())

# Informações gerais do dataset
print(df.info())

# Estatísticas descritivas
print(df.describe())

# Filtrando alunos aprovados (nota >= 6)
aprovados = df[df["nota"] >= 6]
print(f"Aprovados: {len(aprovados)}")

# Média por disciplina
media_por_disciplina = df.groupby("disciplina")["nota"].mean()
print(media_por_disciplina)

# Alunos com maior nota em cada disciplina
melhores = df.loc[df.groupby("disciplina")["nota"].idxmax()]
print(melhores[["nome", "disciplina", "nota"]])

#erro FileNotFoundError: [Errno 2] No such file or directory: 'notas_alunos.csv'
#Esse erro ocorre porque o arquivo 'notas_alunos.csv' não foi encontrado no diretório onde o script está sendo executado.