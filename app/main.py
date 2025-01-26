from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

# Importar os modelos e o blueprint
from app.db.models import db
from app.api.user_verification import user_verification

# Inicialização do app
app = Flask(__name__)
CORS(app)

# Configurações do banco de dados
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(BASE_DIR, 'db/database.sqlite')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar banco de dados com o app Flask
db.init_app(app)

# Registrar o blueprint
app.register_blueprint(user_verification)

# Criar banco de dados automaticamente na primeira execução
@app.before_first_request
def create_tables():
    db.create_all()

# Rota principal
@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to Security Management Solutions!",
        "status": "OK"
    })

# Inicializando o servidor
if __name__ == '__main__':
    app.run(debug=True)
