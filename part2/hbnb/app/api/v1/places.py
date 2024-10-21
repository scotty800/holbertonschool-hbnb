from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade
import logging

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
    'amenities': fields.List(fields.String, required=True, description="List of amenities ID's"),
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
        logging.info(f"Données de lieu reçues : {place_data}")
        owner_id = place_data.get('owner_id')
        logging.info(f"Tentative de création d'un lieu pour le propriétaire avec ID : {owner_id}")
            # Vérifiez que l'utilisateur (owner) existe avant d'ajouter le lieu
        try:
            owner = facade.get_user(place_data['owner_id'])
            if not owner:
                logging.warning(f"Owner not found with ID: {owner_id}")
                return {'error': 'Owner not found'}, 400
        
            new_place = facade.create_place(place_data)
            logging.info(f"Place created successfully with ID: {new_place.id}")
            return {"message": "Place created successfully", "id": new_place.id}, 201
        except ValueError as ve:
            logging.error(f"Invalid input data: {str(ve)}")
            return {"error": f"Invalid input data: {str(ve)}"}, 400
        except Exception as e:
            logging.error(f"Unexpected error: {str(e)}")
            return {"error": f"Internal server error: {str(e)}"}, 500

    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """Retrieve a list of all places"""
        try:
            list_of_all_places = facade.get_all_places()
            return [place for place in list_of_all_places], 200
        except ValueError as e:
            logging.error(f"Failed to retrieve places: {str(e)}")
            return {"error: list_of_all_places"},

@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get place details by ID"""
        # Placeholder for the logic to retrieve a place by ID, including associated owner and amenities
        try:
            place = facade.get_place(place_id)
            if not place:
                logging.warning(f"Place with ID {place_id} not found.")
                return {"error": "Place not found"}, 404

            # Prepare the response with place details
            response = {
                "id": place_id,
                "title": place.title,
                "description": place.description,
                "price": place.price,
                "latitude": place.latitude,
                "longitude": place.longitude,
                "owner": {
                    "id": place.owner.id,
                    "first_name": place.owner.first_name,
                    "last_name": place.owner.last_name,
                    "email": place.owner.email
                },
                "amenities": [amenity.id for amenity in place.amenities]  # Assuming amenities are objects
            }
            return response, 200
        except ValueError as ve:
            logging.error(f"Error retrieving place details: {str(ve)}")
            return {"error": f"Unable to retrieve place: {str(ve)}"}, 500

    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    def put(self, place_id):
        """Update a place's information"""
        # Placeholder for the logic to update a place by ID
        place_data = api.payload
        try:
            update_place = facade.update_place(place_id, place_data)
            if update_place is None:
                return {"error": "Place not found"}, 404
            return {'Place updated successfully'}, 200
        except ValueError as ve:
            logging.error(f"Invalid input data: {str(ve)}")
            return {"error": "invalid input data"}, 400