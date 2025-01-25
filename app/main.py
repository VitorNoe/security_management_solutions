from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

# Importar os modelos
from app.db.models import db, User, LoginAttempt, SuspiciousActivity, AccessLog

# Inicialização do app
app = Flask(__name__)
CORS(app)

# Configurações do banco de dados
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(BASE_DIR, 'db/database.sqlite')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar banco de dados com o app Flask
db.init_app(app)

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

# Rota para verificar segurança do usuário
@app.route('/api/check_account', methods=['POST'])
def check_account():
    data = request.json
    username = data.get('username')

    # Simulação de lógica para verificar a conta
    if not username:
        return jsonify({"error": "Username is required"}), 400

    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({
            "message": f"Account {username} is secure.",
            "last_access": user.last_access
        }), 200
    else:
        return jsonify({"message": f"Account {username} not found."}), 404

# Inicializando o servidor
if __name__ == '__main__':
    app.run(debug=True)
