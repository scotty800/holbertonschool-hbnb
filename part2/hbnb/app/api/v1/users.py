from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade
from flask import request
import re

api = Namespace('users', description='User operations')

# Define the user model for input validation and documentation
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'is_owner': fields.Boolean(required=False, description='Owner of the user ', default=False)
})

facade = HBnBFacade()

def is_valid_email(email):
    """Validate email format."""
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None


@api.route('/', methods=['POST'])
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new user"""

        if not request.is_json:
            return {"error": "Content-Type must be application/json"}, 415

        user_data = request.get_json()

        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            return {'error': 'Email already registered'}, 400

        user_data['is_owner'] = user_data.get('is_owner', False)
        try:
            new_user = facade.create_user(user_data)
            return new_user.to_dict(), 201
        except ValueError as e:
            return {'error': str(e)}, 400
        except Exception as e:
            return {"error": "Internal server error"}, 500

@api.route('/<user_id>')
class UserResource(Resource):
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID"""
        try:
            user = facade.get_user(user_id)
            print("dictinnaire api user")
            if not user:
                return {'error': 'User not found'}, 404
            return user.to_dict(), 200
            
        except Exception as e:
            print(f'An unexpected error occurred: {e}')
            return {'error': 'Internal server error'}, 500
    
    @api.expect(user_model, validate=True)
    @api.response(200, 'User successfully updated')
    @api.response(404, 'User not found')
    @api.response(400, 'Invalid input data')
    @api.response(415, 'Unsupported Media Type')

    def put(self, user_id):
        """Update user details by ID"""

        if not request.is_json:
            return {"error": "Content-Type must be application/json"}, 415
        
        user_data = request.get_json()
        user = facade.get_user(user_id)

        if 'email' in user_data and not is_valid_email(user_data['email']):
            return {'error': 'Invalid email format'}, 400

        if not isinstance(user_data, dict):
            return {"error": "Invalid input data in"}, 400

        if 'email' in user_data:
            existing_user = facade.get_user_by_email(user_data['email'])
            if existing_user and existing_user.id != user_id:
                return {"error": "Email already registered by another user"}, 400
        
        if 'is_owner' not in user_data:
            user_data['is_owner'] = user['is_owner']

        try:
            updated_user = facade.update_user(user_id, user_data)
        except ValueError as error:
            return {"error": str(error)}, 400
        
        print("dictionnaire update api user")

        if not updated_user:
            return {'error': 'User not found'}, 404
        return {
        'id': updated_user.id,
        'first_name': updated_user.first_name,
        'email': updated_user.email,
        'last_name': updated_user.last_name
        }, 200