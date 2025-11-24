import os
from flask import Flask, request, jsonify, session

app = Flask(__name__)
import os
app.secret_key = os.getenv("SECRET_KEY", "dev_key")

users_db = {
    "admin": "admin",
    "Jharvy": "20210184E"
}

products_db = {
    101: {"name": "Monitor 24in", "price": 250.00},
    102: {"name": "HDMI Cable", "price": 20.50},
    103: {"name": "Teclado Mecánico", "price": 85.00}
}

@app.route('/')
def index():
    return 'Web App de la PC4'

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status" : "ok",
                    "message": "La aplicacion esta funcionando correctamente"}), 200

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({"status" : "error",
                        "message": "No se proporciono un usuario o contrasena"}), 400
    
    if username in users_db and users_db[username] == password:
        session['user'] = username
        return jsonify({"status" : "ok",
                        "message": "Login exitoso"}), 200
    
    return jsonify({"status" : "error",
                    "message": "Usuario o contrasena incorrectos"}), 401

@app.route('/cart', methods=['GET'])
def get_products():
    if 'user' not in session:
        return jsonify({"status" : "error",
                        "message": "Usuario no autenticado"}), 401

    total = 0
    for product in products_db.values():
        total += product['price']

    return jsonify({"user" : session['user'],
                    "message": "Lista de productos",
                    "products": products_db,
                    "total": total}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)