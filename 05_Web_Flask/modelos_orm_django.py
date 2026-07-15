from django.db import models

# Definição do modelo (classe = tabela no banco)
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True)
    curso = models.CharField(max_length=100)
    data_ingresso = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.matricula}"

# Queries declarativas com o ORM
# Buscar todos os alunos de Computação
alunos_cc = Aluno.objects.filter(curso="Ciência da Computação")

# Buscar um aluno específico
aluno = Aluno.objects.get(matricula="2024001")

# Criar novo aluno
novo = Aluno.objects.create(
    nome="Carla Silva",
    matricula="2024050",
    curso="Eng. de Software"
)

#o erro o Django está dizendo que você tentou criar um modelo de aluno (class Aluno), 
# mas ele não sabe onde salvar isso porque não existe um arquivo de configuração (settings.py) dizendo qual é o banco de dados (SQLite, MySQL, etc.) 
# e nem se o aplicativo está "instalado" no projeto.