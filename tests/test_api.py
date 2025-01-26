import unittest
from flask import json
from app import app, db
from app.db.models import User, LoginAttempt, SuspiciousActivity

class TestAPI(unittest.TestCase):
    def setUp(self):
        """
        Configura o ambiente de teste.
        """
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"  # Banco de dados em memória
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        """
        Limpa o ambiente de teste.
        """
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_register_user(self):
        """
        Testa a funcionalidade de registro de um usuário.
        """
        response = self.app.post('/api/register', json={
            'username': 'test_user',
            'email': 'test_user@example.com',
            'password': 'securepassword'
        })
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['message'], "User test_user registered successfully")

    def test_register_duplicate_user(self):
        """
        Testa o registro de um usuário com dados duplicados.
        """
        self.app.post('/api/register', json={
            'username': 'test_user',
            'email': 'test_user@example.com',
            'password': 'securepassword'
        })
        response = self.app.post('/api/register', json={
            'username': 'test_user',
            'email': 'test_user@example.com',
            'password': 'securepassword'
        })
        self.assertEqual(response.status_code, 409)
        data = json.loads(response.data)
        self.assertIn("Username or email already exists", data['error'])

    def test_check_account(self):
        """
        Testa a verificação de segurança de uma conta.
        """
        self.app.post('/api/register', json={
            'username': 'test_user',
            'email': 'test_user@example.com',
            'password': 'securepassword'
        })
        response = self.app.post('/api/check_account', json={'username': 'test_user'})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['message'], "Account test_user is secure.")

    def test_login_attempt(self):
        """
        Testa o registro de uma tentativa de login.
        """
        self.app.post('/api/register', json={
            'username': 'test_user',
            'email': 'test_user@example.com',
            'password': 'securepassword'
        })
        response = self.app.post('/api/login_attempt', json={
            'username': 'test_user',
            'status': 'success'
        })
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['message'], "Login attempt for test_user registered successfully")

    def test_get_suspicious_activities(self):
        """
        Testa a obtenção de atividades suspeitas.
        """
        with app.app_context():
            user = User(username='test_user', email='test_user@example.com', password='securepassword')
            db.session.add(user)
            db.session.commit()

            activity = SuspiciousActivity(user_id=user.id, description="Suspicious login detected")
            db.session.add(activity)
            db.session.commit()

        response = self.app.get('/api/suspicious_activities')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data['suspicious_activities']), 1)
        self.assertEqual(data['suspicious_activities'][0]['description'], "Suspicious login detected")

if __name__ == '__main__':
    unittest.main()
