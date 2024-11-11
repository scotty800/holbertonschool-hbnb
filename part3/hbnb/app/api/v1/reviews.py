from flask_restx import Namespace, Resource, fields
from app.services import facade
from app.services.facade import HBnBFacade
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services import facade
from flask import request


api = Namespace('reviews', description='Review operations')

@api.route('/reviews/')
class ReviewList(Resource):
    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        place_id = request.json.get("place_id")
        place = facade.get_place(place_id)
        if place.owner_id == current_user:
            return {'error': 'You cannot review your own place'}, 400
        if facade.user_already_reviewed_place(current_user, place_id):
            return {'error': 'You have already reviewed this place'}, 400
        pass


@api.route('/reviews/<review_id>')
class ReviewResource(Resource):
    @jwt_required()
    def put(self, review_id):
        current_user = get_jwt_identity()
        review = facade.get_review(review_id)
        if review.user_id != current_user:
            return {'error': 'Unauthorized action'}, 403
        pass


    @jwt_required()
    def delete(self, review_id):
        current_user = get_jwt_identity()
        review = facade.get_review(review_id)
        if review.user_id != current_user:
            return {'error': 'Unauthorized action'}, 403
        pass