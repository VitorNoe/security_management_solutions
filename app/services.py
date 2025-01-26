from app.db.models import db, User, LoginAttempt, SuspiciousActivity, AccessLog
from datetime import datetime

# Serviço para registrar um novo usuário
def register_user_service(username, email, password):
    # Verificar se o usuário já existe
    if User.query.filter((User.username == username) | (User.email == email)).first():
        return {"error": "Username or email already exists"}, 409

    # Criar novo usuário
    new_user = User(username=username, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()
    return {"message": f"User {username} registered successfully"}, 201

# Serviço para verificar a segurança de uma conta
def check_account_service(username, ip_address):
    user = User.query.filter_by(username=username).first()
    if not user:
        return {"error": f"Account with username {username} not found"}, 404

    # Registrar log de acesso
    access_log = AccessLog(user_id=user.id, ip_address=ip_address)
    db.session.add(access_log)
    db.session.commit()

    return {
        "message": f"Account {username} is secure.",
        "last_access": user.last_access,
        "access_logs": len(user.access_logs)
    }, 200

# Serviço para registrar tentativas de login
def login_attempt_service(username, ip_address, status):
    user = User.query.filter_by(username=username).first()
    if not user:
        return {"error": f"Account with username {username} not found"}, 404

    # Registrar tentativa de login
    attempt = LoginAttempt(user_id=user.id, ip_address=ip_address, status=status)
    db.session.add(attempt)
    db.session.commit()
    return {"message": f"Login attempt for {username} registered successfully"}, 201

# Serviço para listar atividades suspeitas
def get_suspicious_activities_service():
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
    return {"suspicious_activities": activities}, 200
