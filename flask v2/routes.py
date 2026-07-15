#importanto arquivo main para acessar a aplicação criada nele
from main import app

@app.route("/")
def homepage():
    return "Olá, Alunos!"

#definindo uma nova rota para a página 2
@app.route("/page2")
def page2():
    return "Olá Professsor, Ana aqui, tudo bem?"
