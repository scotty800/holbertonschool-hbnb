from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.services import facade
from app.services.facade import HBnBFacade
print(f'facade: {HBnBFacade}')
# Namespace for authentication
api = Namespace('auth', description='Authentication operations')

facade = HBnBFacade()
# Model for input validation
login_model = api.model('Login', {
    'email': fields.String(required=True, description='User email'),
    'password': fields.String(required=True, description='User password')
})

@api.route('/login')
class Login(Resource):
    @api.expect(login_model)
    def post(self):
        """Authenticate user and return a JWT token"""
        credentials = api.payload  # Get the email and password from the request payload

        # Retrieve the user based on the provided email
        user = facade.get_user_by_email(credentials['email'])

        # Check if the user exists and the password is correct
        if not user or not user.verify_password(credentials['password']):
            return {'error': 'Invalid credentials'}, 401

        try:
            # Create a JWT token with the user's id and is_admin flag
            access_token = create_access_token(identity={'id': str(user.id), 'is_admin': user.is_admin})
            return {'access_token': access_token}, 200
        except Exception as e:
            print(f"Erreur lors de l'authentification : {str(e)}")
            return {"error": "Erreur d'authentification"}, 500


@api.route('/')
class ProtectedResource(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        return {'message': f'Hello, user {current_user["id"]}'}, 200
