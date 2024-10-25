from flask import Flask
from flask_restx import Api
from app.api.v1.users import api as users_ns
from app.api.v1.places import api as places_api
from app.api.v1.amenities import api as aminity_api

def create_app():
    app = Flask(__name__)
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API')

    api.add_namespace(places_api, path='/api/v1/places')
    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(aminity_api, path='/api/v1/amenities')

    return app