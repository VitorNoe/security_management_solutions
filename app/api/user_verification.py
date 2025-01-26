from flask import Blueprint, jsonify, request
from datetime import datetime
from app.db.models import db, User, LoginAttempt, SuspiciousActivity, AccessLog

# Criando um blueprint para as APIs de verificação
user_verification = Blueprint('user_verification', __name__)

# Rota para registrar um novo usuário
@user_verification.route('/api/register', methods=['POST'])
def register_user():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({"error": "All fields are required: username, email, and password"}), 400

    # Verificar se o usuário já existe
    if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
        return jsonify({"error": "Username or email already exists"}), 409

    # Criar novo usuário
    new_user = User(username=username, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": f"User {username} registered successfully"}), 201

# Rota para verificar a segurança de uma conta
@user_verification.route('/api/check_account', methods=['POST'])
def check_account():
    data = request.json
    username = data.get('username')

    if not username:
        return jsonify({"error": "Username is required"}), 400

    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"error": f"Account with username {username} not found"}), 404

    # Adicionar registro no log de acessos
    access_log = AccessLog(user_id=user.id, ip_address=request.remote_addr)
    db.session.add(access_log)
    db.session.commit()

    return jsonify({
        "message": f"Account {username} is secure.",
        "last_access": user.last_access,
        "access_logs": len(user.access_logs)
    }), 200

# Rota para registrar tentativa de login
@user_verification.route('/api/login_attempt', methods=['POST'])
def login_attempt():
    data = request.json
    username = data.get('username')
    status = data.get('status')  # "success" ou "failed"

    if not username or not status:
        return jsonify({"error": "Username and status are required"}), 400

    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"error": f"Account with username {username} not found"}), 404

    # Registrar tentativa de login
    attempt = LoginAttempt(user_id=user.id, ip_address=request.remote_addr, status=status)
    db.session.add(attempt)
    db.session.commit()

    return jsonify({"message": f"Login attempt for {username} registered successfully"}), 201

# Rota para listar atividades suspeitas
@user_verification.route('/api/suspicious_activities', methods=['GET'])
def get_suspicious_activities():
    suspicious_activities = SuspiciousActivity.query.all()
    activities = [
        {
            "id": activity.id,
            "user_id": activity.user_id,
            "description": activity.description,
            "detected_at": activity.detected_at
        }
        for activity in suspicious_activities
    ]

    return jsonify({"suspicious_activities": activities}), 200
