from flask_restx import Namespace, Resource, fields
from app.services import facade
from app.services.facade import HBnBFacade


api = Namespace('reviews', description='Review operations')

# Define the review model for input validation and documentation
review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'user_id': fields.String(required=True, description='ID of the user'),
    'place_id': fields.String(required=True, description='ID of the place')
})

@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new review"""
        review_data = api.payload

        if not review_data:
            return {'error': 'Invalid input data'}, 400

        try:
            new_review = facade.create_review(review_data)
        except ValueError as e:
            return {'error': str(e)}, 400
        except Exception as e:
            return {'error': 'An unexpected error occurred'}, 500
        return {'message': 'Review successfully created', 'review': new_review}, 201


    @api.response(200, 'List of reviews retrieved successfully')
    def get(self):
        """Retrieve a list of all reviews"""
        try:
            list_review = facade.get_all_reviews()
            if not list_review:
                return {'message': 'No reviews found'}, 200
        # Retourner la liste des reviews
            return {'reviews': list_review}, 200

        except Exception as e:
        # Gestion des erreurs inattendues
            return {'error': 'An unexpected error occurred'}, 500

@api.route('/<review_id>')
class ReviewResource(Resource):
    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    def get(self, review_id):
        """Retrieve details of a specific review by ID"""
        try:
            review = facade.get_review(review_id)
            if not review:
                return {'error': 'Review not found'}, 404
            return {
                'id': review.id,
                'user_id': review.user_id,
                'place_id': review.place_id,
                'text': review.text,
                'rating': review.rating,
                'created_at': review.created_at,
                'updated_at': review.updated_at
            }, 200

        except Exception as e:
            return {'error': 'An unexpected error occurred'}, 500


    @api.expect(review_model)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(400, 'Invalid input data')
    def put(self, review_id):
        """Update a review's information"""
        review_data = api.payload
        if not review_data:
            return {'error': 'Invalid input data'}, 400

        try:
            review = facade.get_review(review_id)
            if not review:
                return {'error': 'Review not found'}, 404
            if 'text' in review_data:
                review.text = review_data['text']
            if 'rating' in review_data:
                review.rating = review_data['rating']
            updated_review = facade.update_review(review_id, review_data)

            return {
                'id': updated_review.id,
                'user_id': updated_review.user_id,
                'place_id': updated_review.place_id,
                'text': updated_review.text,
                'rating': updated_review.rating,
                'created_at': updated_review.created_at,
                'updated_at': updated_review.updated_at
                }, 200

        except ValueError as e:
            return {'error': str(e)}, 400
        except Exception as e:
            return {'error': 'An unexpected error occurred'}, 500

    @api.response(200, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    def delete(self, review_id):
        """Delete a review"""
        try:
            review = facade.get_review(review_id)
            if not review:
                return {'error': 'Review not found'}, 404
            facade.delete_review(review_id)

            return {'message': 'Review deleted successfully'}, 200

        except Exception as e:
            return {'error': 'An unexpected error occurred'}, 500

@api.route('/places/<place_id>/reviews')
class PlaceReviewList(Resource):
    @api.response(200, 'List of reviews for the place retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get all reviews for a specific place"""
        try:
            place = facade.get_place(place_id)

            if not place:
                return {'error': 'Place not found'}, 404

            reviews = facade.get_reviews_by_place(place_id)

            if not reviews:
                return {'message': 'No reviews found for this place'}, 200

            return {'reviews': reviews}, 200

        except Exception as e:
            return {'error': 'An unexpected error occurred'}, 500