from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade
from flask import request
api = Namespace('amenities', description='Amenity operations')

# Define the amenity model for input validation and documentation
amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})

facade = HBnBFacade()

@api.route('/')
class AmenityList(Resource):
    @api.expect(amenity_model)
    @api.response(201, 'Amenity successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new amenity"""
        amenity_data = api.payload
        new_amenity = facade.create_amenity(amenity_data)
        if new_amenity:
            return {'id': new_amenity['id'], 'name': new_amenity['name']}, 201
        else:
            return {'message': 'Amenity creation failed'}, 400
    @api.response(200, 'List of amenities retrieved successfully')
    def get(self):
        """Retrieve a list of all amenities"""
        amenities_list = facade.get_all_amenities()
        return [{'id': amenity.id, 'name': amenity.name} for amenity in amenities_list ], 200


@api.route('/<amenity_id>')
class AmenityResource(Resource):
    @api.response(200, 'Amenity details retrieved successfully')
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """Get amenity details by ID"""
        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            return {'error': 'Amenity not found'}, 404
        return {"id": amenity_id, 'name': amenity.name}, 200

    @api.expect(amenity_model)
    @api.response(200, 'Amenity updated successfully')
    @api.response(404, 'Amenity not found')
    @api.response(400, 'Invalid input data')
    def put(self, amenity_id):
        """Update an amenity's information"""
        amenity_data = api.payload
        updated = facade.update_amenity(amenity_id, amenity_data)

        if not updated:
            return {'error': 'Amenity not found'}, 404
        else:
            return {'message': 'Amenity updated successfully'}, 200