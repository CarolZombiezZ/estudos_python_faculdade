from flask import Flask, jsonify, request

app = Flask(__name__)

# Banco de dados simulado em memória
usuarios = [
    {"id": 1, "nome": "Ana", "curso": "Eng. de Software"},
    {"id": 2, "nome": "Bruno", "curso": "Ciência da Computação"},
    {"id": 3, "nome": "Solaire", "curso": "ADS"},
]

# Rota GET: retorna todos os usuários
@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    return jsonify(usuarios)

# Rota POST: adiciona novo usuário
@app.route("/usuarios", methods=["POST"])
def criar_usuario():
    dados = request.json
    novo = {"id": len(usuarios) + 1, **dados}
    usuarios.append(novo)
    return jsonify(novo), 201

if __name__ == "__main__":
    app.run(debug=True)

#abrindo no chrome esse link http://127.0.0.1:5000/usuarios vai mostrar a lista de usuários cadastrados.
#onde criamos uma lista simples de usuários e duas rotas: uma para listar os usuários (GET) e outra para criar um novo usuário (POST).