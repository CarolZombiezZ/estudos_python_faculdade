#Prática 1 — Web (Flask)
#importando framework
from flask import Flask

#criando a aplicação
app = Flask(__name__)

#rotas definindo a rota principal do site, ou seja, a página inicial
@app.route("/")
#criando a função que será executada quando a rota for acessada
def homepage():
    #retornando uma mensagem para o navegador
    return "Olá, Alunos!"

#para função não ser executada quando o módulo for importado, mas apenas quando for executado diretamente
if __name__ == "__main__":
#iniciando o servidor para que a aplicação possa ser acessada
    app.run()
