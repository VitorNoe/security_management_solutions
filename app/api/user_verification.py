from flask import Blueprint, jsonify, request
from app.services import (
    register_user_service,
    check_account_service,
    login_attempt_service,
    get_suspicious_activities_service,
)

user_verification = Blueprint('user_verification', __name__)

@user_verification.route('/api/register', methods=['POST'])
def register_user():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    return register_user_service(username, email, password)

@user_verification.route('/api/check_account', methods=['POST'])
def check_account():
    data = request.json
    username = data.get('username')
    ip_address = request.remote_addr
    return check_account_service(username, ip_address)

@user_verification.route('/api/login_attempt', methods=['POST'])
def login_attempt():
    data = request.json
    username = data.get('username')
    status = data.get('status')
    ip_address = request.remote_addr
    return login_attempt_service(username, ip_address, status)

@user_verification.route('/api/suspicious_activities', methods=['GET'])
def get_suspicious_activities():
    return get_suspicious_activities_service()
