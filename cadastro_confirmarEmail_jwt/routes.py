from flask import request, jsonify
from app import app, db, mail
from models import User
from flask_jwt_extended import create_access_token
from flask_mail import Message
from flask_jwt_extended import decode_token

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"message": "Email já registrado."}), 400
    
    user = User(email=data['email'], password=data['password'])
    db.session.add(user)
    db.session.commit()
    
    token = create_access_token(identity=user.email)
    confirm_link = f"http://localhost:5000/confirm/{token}"
    send_confirmation_email(user.email, confirm_link)
    
    return jsonify({"message": "Usuário registrado. Confirme seu email."}), 201

@app.route('/confirm/<token>', methods=['GET'])
def confirm_email(token):
    try:
        email = decode_token(token)['sub']
        user = User.query.filter_by(email=email).first()
        if user:
            user.confirmed = True
            db.session.commit()
            return jsonify({"message": "Email confirmado!"})
    except Exception as e:
        return jsonify({"message": "Token inválido!"}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email'], password=data['password']).first()
    if user and user.confirmed:
        token = create_access_token(identity=user.email)
        return jsonify({"token": token})
    return jsonify({"message": "Credenciais inválidas ou email não confirmado."}), 401

@app.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    users_list = [{"id": user.id, "email": user.email, "confirmed": user.confirmed} for user in users]
    return jsonify(users_list), 200

@app.route('/users', methods=['DELETE'])
def delete_all_users():
    try:
        num_rows_deleted = db.session.query(User).delete()
        db.session.commit()
        return jsonify({"message": f"{num_rows_deleted} usuários deletados."}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Erro ao deletar usuários."}), 500

def send_confirmation_email(to_email, link):
    msg = Message('Confirme seu cadastro', sender='jgadgaambrosio@gmail.com', recipients=[to_email])
    msg.body = f'Clique no link para confirmar seu cadastro: {link}'
    mail.send(msg)