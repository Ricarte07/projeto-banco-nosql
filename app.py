from flask import Flask, jsonify, render_template
from pymongo import MongoClient
from bson import json_util # Ajuda a converter dados do MongoDB para JSON

# 1. Iniciar o Flask
app = Flask(__name__)

# 2. Conectar ao MongoDB (verifique se o seu container Docker está rodando!)
client = MongoClient('mongodb://localhost:27017/')
db = client.MeuApp # Nome do banco de dados que criamos
collection = db.usuarios # Nome da coleção

# 3. Criar a rota para o "Restaurante" (a página principal)
@app.route('/')
def index():
    # Esta função simplesmente serve o arquivo index.html para o cliente
    return render_template('index.html')

# 4. Criar a rota da API que entrega os dados dos usuários
@app.route('/api/usuarios')
def get_usuarios():
    # Busca todos os documentos na coleção 'usuarios'
    usuarios = list(collection.find({}))
    
    # Converte os dados do MongoDB para um formato JSON que a web entende
    # O json_util cuida do formato especial do _id do MongoDB
    return json_util.dumps(usuarios)

# 5. Rodar o servidor
if __name__ == '__main__':
    app.run(debug=True)