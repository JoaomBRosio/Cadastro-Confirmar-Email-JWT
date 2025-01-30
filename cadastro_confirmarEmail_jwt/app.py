from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_mail import Mail
import os

# Inicializa o Flask
app = Flask(__name__)

# Caminho do banco de dados
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE_PATH = os.path.join(BASE_DIR, 'database', 'users.db')

# Garante que o diretório do banco de dados existe
os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)

# Configurações do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DATABASE_PATH}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configurações do JWT
app.config['JWT_SECRET_KEY'] = 'super-secret-key'
jwt = JWTManager(app)

# Configuração do Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'jgadgaambrosio@gmail.com'
app.config['MAIL_PASSWORD'] = 'qghu hciv bxbe ynkk'  # Substitua por uma senha real ou App Password

mail = Mail(app)
db = SQLAlchemy(app)

from routes import *

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Cria as tabelas do banco ao iniciar
    app.run(debug=True)
