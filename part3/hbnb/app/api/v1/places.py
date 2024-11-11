from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services import facade

api = Namespace('places', description='Place operations')

@api.route('/')
class PlaceList(Resource):
    @jwt_required()
    def post(self):
        """Create a new place"""
        current_user = get_jwt_identity()
        # Logic to create a new place for the logged-in user
        pass



@api.route('/<place_id>')
class PlaceResource(Resource):
    @jwt_required()
    def put(self, place_id):
        current_user = get_jwt_identity()
        place = facade.get_place(place_id)
        if place.owner_id != current_user:
            return {'error': 'Unauthorized action'}, 403
        # Logic to update the place
        pass
