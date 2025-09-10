from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flasgger import Swagger
from bs4 import BeautifulSoup 

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

#------------------------------------------------------------

@app.route('/')
def home():
    return "Hello, Flask!"

items = []

@app.route('/items', methods=['GET'])
def get_items():
   return jsonify (items)


@app.route('/items', methods=['POST']) # envia JSON no corpo 
def create_item():
    data = request.get_json() #captura o corpo da requisicao
    items.append(data)  # adicioa o item a lista de items
    return jsonify((data)), 201 #201 retorna status

@app.route('/items/<int:item_id>', methods=['PUT']) # identificacao do item pelo indice <int:item_id>
def update_item (item_id):
    data = request.get_json() #data obtida do JSON para atualizar o item 
    if 0 <= item_id < len(items): # checa se o item_id esta em intervalo valido, caso ok, atualiza e retorna o item
        return jsonify(items[item_id])
    return jsonify ({"error: Item not found"}), 404 #se nao existir, retorna o erro 404

@app.route ('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id): #remove e retorna o item na posicao
    if 0<= item_id < len (items):
        removed = items.pop(item_id)
        return jsonify(removed) #retorna o objeto deletado como confirmacao
    return jsonify ({"error: Item not found"}), 404 #verifica se o indice esta no intervalo para evitar erro, caso nao exista retorna 404
#------------
#aula2 - parte 3 
def get_title(url):
    try:
          response = request.get(url)
          soup = BeautifulSoup(response.text, 'html.parser')
          title = soup.title.string.strip()
          return jsonify ({"title": title})
    except Exception as e:
         return jsonify ({"error": str(e)}),500
@app.route('/scrape/title',methods=['GET'])
@auth.login_required

def scrape_title():
    """
    Extract the title of a web page provided by the URL.
    ---
    security:
        -BasicAuth:[]
    parameters:
        -name:url
        in:query
        type:string
        required:true
        description: URL of the web page
    responses:
        200:
            description: Web page title
    """
    url = request.args.get('url')
    if not url:
        return jsonify({"error":"URL is required"}), 400
    return get_title(url)

if __name__== '__main__':
    app.run(debug=True)