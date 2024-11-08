from flask import Flask
from config import DevelopmentConfig
from flask_jwt_extended import JWTManager
from api.v1.auth import api as auth_namespace
from flask_bcrypt import Bcrypt
from flask import Flask
from flask_restx import Api

bcrypt = Bcrypt()

jwt = JWTManager()

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    bcrypt.init_app(app)
    jwt.init_app(app)
    api = Api(app)
    @app.route('/')
    def home():
        return "Hello, world!"
    
    api.add_namespace(auth_namespace, path='/api/v1/auth')

    return app