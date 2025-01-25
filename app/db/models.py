from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# Modelo para usuários registrados
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    last_access = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f"<User {self.username}>"

# Modelo para monitorar tentativas de login
class LoginAttempt(db.Model):
    __tablename__ = 'login_attempts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    attempt_time = db.Column(db.DateTime, default=datetime.utcnow)
    ip_address = db.Column(db.String(45), nullable=True)
    status = db.Column(db.String(20), nullable=False)  # Ex.: "success", "failed"

    # Relacionamento com o usuário
    user = db.relationship('User', backref=db.backref('login_attempts', lazy=True))

    def __repr__(self):
        return f"<LoginAttempt User ID: {self.user_id}, Status: {self.status}>"

# Modelo para atividades suspeitas
class SuspiciousActivity(db.Model):
    __tablename__ = 'suspicious_activities'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    detected_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relacionamento com o usuário
    user = db.relationship('User', backref=db.backref('suspicious_activities', lazy=True))

    def __repr__(self):
        return f"<SuspiciousActivity User ID: {self.user_id}, Description: {self.description}>"

# Modelo para logs de acesso (histórico de acessos)
class AccessLog(db.Model):
    __tablename__ = 'access_logs'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    access_time = db.Column(db.DateTime, default=datetime.utcnow)
    ip_address = db.Column(db.String(45), nullable=True)

    # Relacionamento com o usuário
    user = db.relationship('User', backref=db.backref('access_logs', lazy=True))

    def __repr__(self):
        return f"<AccessLog User ID: {self.user_id}, Access Time: {self.access_time}>"
