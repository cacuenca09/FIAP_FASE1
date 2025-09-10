from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flasgger import Swagger 

app = Flask(__name__)

app.config['SWAGGER'] = {
        'title': 'My Flask API',
        'uiversion': 3
}
swagger = Swagger(app) 
# o acesso a documentacao vai ser via api doc ou flasgger (dependendo da versao)

auth = HTTPBasicAuth()

#Dicionario users simulando um "banco" de credenciais
users = {
    "user1": "password1",
    "user2": "password2"
}

#Funcao verify_password para validar usuario e senha, retornando o username se coreeto, caso contrario, none, 
#e toda rota com @auth.login_required exigira credenciais
@auth.verify_password
def verify_password(username,password):
        return username

#proteger a rota
@app.route ('/hello', methods=['GET'])
@auth.login_required
def hello():
        return jsonify ({"message":"Hello, Wordl!"})

if __name__ == '__main':
        app.run(debug=True)