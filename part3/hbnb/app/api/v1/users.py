from flask import request, jsonify
from app import db
from models.user import User
from app import create_app, db
from models.user import User
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services import facade
from flask_restx import Api, Namespace
app = create_app()
api = Api(app)  # Initialise l'API avec l'application Flask
user_ns = Namespace('users', description='User operations')  # Création d'un namespace pour les utilisateurs
api.add_namespace(user_ns, path='/api/v1')

@app.route('/api/v1/users/', methods=['POST'])
def create_user():
    data = request.get_json()

    if not data or not data.get('email') or not data.get('password'):
        return jsonify({"message": "Missing required fields"}), 400

    user = User(email=data['email'])
    user.hash_password(data['password'])

    db.session.add(user)
    db.session.commit()

    return jsonify({"id": user.id, "email": user.email}), 201


@app.route('/api/v1/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)

    user_data = {
        'id': user.id,
        'email': user.email,
    }

    return jsonify(user_data), 200


@api.route('/users/<user_id>')
class UserResource(Resource):
    @jwt_required()
    def put(self, user_id):
        current_user = get_jwt_identity()
        if current_user != user_id:
            return {'error': 'Unauthorized action'}, 403
        data = request.json
        if 'email' in data or 'password' in data:
            return {'error': 'You cannot change your email or password'}, 400
        pass

@api.route('/places/')
class PublicPlaces(Resource):
    def get(self):
        pass

