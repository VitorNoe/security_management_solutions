from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para verificar segurança
@app.route('/check', methods=['POST'])
def check():
    user_input = request.form.get('username')
    # Placeholder para verificar segurança
    security_status = "Seguro"  # Exemplo: pode ser substituído por uma lógica real
    return f"A conta '{user_input}' está {security_status}!"

if __name__ == '__main__':
    app.run(debug=True)
