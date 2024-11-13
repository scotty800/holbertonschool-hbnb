from flask import Flask
from flask_restx import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
jwt = JWTManager()
bcrypt = Bcrypt()

def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)
    print("Debug mode:", app.config['DEBUG'])
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialiser les extensions avec l'application
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Importer et ajouter les namespaces de l'API
    from app.api.v1.users import api as users_ns
    from app.api.v1.places import api as places_api
    from app.api.v1.amenities import api as aminity_api
    from app.api.v1.reviews import api as reviews_ns
    from app.api.v1.auth import api as auth_api

    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API')

    api.add_namespace(auth_api, path='/api/v1/auth')
    api.add_namespace(places_api, path='/api/v1/places')
    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(aminity_api, path='/api/v1/amenities')
    api.add_namespace(reviews_ns, path='/api/v1/reviews')

    return app
