from flask import Flask, jsonify, render_template
from pymongo import MongoClient
from bson import json_util # Ajuda a converter dados do MongoDB para JSON

# 1. Iniciar o Flask
app = Flask(__name__)

# 2. Conectar ao MongoDB 
client = MongoClient('mongodb://localhost:27017/')
db = client.MeuApp # Nome do banco de dados que criamos
collection = db.usuarios # Nome da coleção

@app.route('/')
def index():
   
    return render_template('index.html')


@app.route('/api/usuarios')
def get_usuarios():
    # Busca todos os documentos na coleção 'usuarios'
    usuarios = list(collection.find({}))
    
    # Converte os dados do MongoDB para um formato JSON que a web entende
    # O json_util cuida do formato especial do _id do MongoDB
    return json_util.dumps(usuarios)



app.run(debug=True)
