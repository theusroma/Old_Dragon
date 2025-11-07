from flask import Flask
from controllers.character_controller import bp as character_bp

def create_app():
    app = Flask(__name__)
    # Chave secreta é necessária para o Flask usar 'flash messages'
    app.secret_key = 'uma-chave-secreta-de-desenvolvimento'
    
    # Registra o controlador (character_bp) na aplicação
    app.register_blueprint(character_bp)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)