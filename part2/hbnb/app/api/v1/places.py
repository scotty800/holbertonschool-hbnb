from flask_restx import Namespace, Resource, fields, abort
from app.services.facade import HBnBFacade
from flask import jsonify, request

api = Namespace('places', description='Place operations')

# Define the models for related entities
amenity_model = api.model('PlaceAmenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Name of the amenity')
})
user_model = api.model('PlaceUser', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='First name of the owner'),
    'last_name': fields.String(description='Last name of the owner'),
    'email': fields.String(description='Email of the owner')
})

# Define the place model for input validation and documentation
place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    'owner': fields.Nested(user_model, description='Owner details'),
    'amenities': fields.List(fields.String, required=False, description="List of amenities ID's"),
})

facade = HBnBFacade()

@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    @api.response(500, 'Internal server error')
    def post(self):
        """Register a new place"""
        place_data = api.payload
        print(f"Received place_data: {place_data}")
        try:
            required_fields = ['owner_id', 'title', 'description', 'price', 'latitude', 'longitude', 'amenities']
            for field in required_fields:
                if field not in place_data:
                    print(f"Missing field: {field}")
                    return {'error': f'Missing field: {field}'}, 400
                owner_id = place_data['owner_id']
                print(f"Attempting to retrieve owner with ID: {owner_id}")
                owner = facade.get_user(owner_id)
                if owner is None:
                    print(f"User not found with ID api place: {owner_id}")
                    return {'error': 'User not found api'}, 404
                print(f"Owner found: {owner}")
                if not owner.get('is_owner', False):
                    print(f"Permission denied for user ID: {owner_id}")
                    return {'error': 'Permission denied: user is not an owner'}, 403
                new_place = facade.create_place(place_data)
                print(f"New place created: {new_place}")
                if not isinstance(new_place, dict):
                    print(f"Unexpected new_place format: {new_place}")
                    return {'error': 'Unexpected error occurred while creating the place'}, 500
                return {
            'id': new_place.get('id'),
            'title': new_place.get('title'),
            'description': new_place.get('description'),
            'price': new_place.get('price'),
            'latitude': new_place.get('latitude'),
            'longitude': new_place.get('longitude'),
            'owner_id': new_place.get('owner_id'),
            'amenities': new_place.get('amenities')
            }, 201
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            return {'error': 'Internal server error'}, 500
        
    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """Retrieve a list of all places"""
        try:
            list_of_all_places = facade.get_all_places()
            return [place.to_dict() for place in list_of_all_places], 200
        except ValueError as e:
            return {"error: list_of_all_places"},

@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get place details by ID"""
        try:
            place = facade.get_place(place_id)
            if not place:
                return {"error": "Place not found"}, 404
            response_data = {
                "id": place['id'],
                "title": place['title'],
                "description": place['description'],
                "price": place['price'],
                "latitude": place['latitude'],
                "longitude": place['longitude'],
                "owner": {
                    "id": place['owner_id'],
                    "first_name": place.owner.first_name,
                    "last_name": place.owner.last_name,
                    "email": place.owner.email
                },
                "amenities": [amenity.id for amenity in place.amenities]
            }
            return response_data, 200
        except ValueError as ve:
            return {"error": f"Unable to retrieve place: {str(ve)}"}, 500

    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    def put(self, place_id):
        """Update a place's information"""
        place_data = api.payload
        try:
            updated_place = facade.update_place(place_id, place_data)
            if updated_place is None:
                return {"error": "Place not found"}, 404
            return {'Place updated successfully'}, 200
        except ValueError as ve:
            return {"error": "invalid input data"}, 400