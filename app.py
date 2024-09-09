from flask import Flask
from flask_cors import CORS

from routes.users import users_bp
from routes.devices import devices_bp

app = Flask(__name__)

# Configuração de CORS, se precisar de opções específicas, configure aqui
CORS(app)

# Registrando os blueprints
app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(devices_bp, url_prefix='/devices')

if __name__ == '__main__':
    # Rodar a aplicação com debug=True apenas para desenvolvimento
    app.run(debug=True)
