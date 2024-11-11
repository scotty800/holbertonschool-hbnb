from flask import Flask
from config import DevelopmentConfig
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

bcrypt = Bcrypt()

jwt = JWTManager()

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    bcrypt.init_app(app)
    jwt.init_app(app)
    app.config["JWT_SECRET_KEY"] = "your_secret_key"
    db.init_app(app)

    @app.route('/')
    def home():
        return "Hello, world!"

    return app