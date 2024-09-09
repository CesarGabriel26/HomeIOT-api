import bcrypt
import jwt
import datetime
from flask import Blueprint, request, jsonify
from models import User
from conection import create_connection, close_connection
import mysql

users_bp = Blueprint('users', __name__)

# Carregar variáveis de ambiente do arquivo .env

# Obter a SECRET_KEY da variável de ambiente
SECRET_KEY = "ae26c5df0cbf451e2504f9ba5ab9d42f191939f65ce8e6a3f94787715db20811"

@users_bp.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    user = User.from_dict(data)

    # Criptografando a senha com bcrypt
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (username, password, email, pfp) VALUES (%s, %s, %s, %s)",
            (user.username, hashed_password, user.email, user.pfp)
        )
        conn.commit()
        
        return jsonify({'message': 'User added successfully', 'user': user.to_dict()})
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500
    finally:
        cursor.close()
        close_connection(conn)

@users_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    useremail = data.get('useremail')
    password = data.get('password')

    conn = create_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM users WHERE email = %s", (useremail,))
        user = cursor.fetchone()
        
        if user:
            if bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
                token = jwt.encode({
                    'user_id': user['id'],
                    'username': user['username'],
                    'password': user['password'],
                    'email': user['email'],
                    'pfp': user['pfp'],
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
                }, SECRET_KEY, algorithm='HS256')

                return jsonify({'token': token}), 200
            else:
                return jsonify({'message': 'Invalid password'}), 401
        else:
            return jsonify({'message': 'User not found'}), 404
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500
    finally:
        cursor.close()
        close_connection(conn)
