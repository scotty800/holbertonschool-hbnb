from flask_restx import Namespace, Resource, fields
from app.services.facade import facade
from flask import request


api = Namespace("users", description="User operations")
# facade = HBnBFacade()  # Creating the instance

# Define the user model for input validation and documentation
user_model = api.model(
    "User",
    {
        "first_name": fields.String(
            required=True, description="First name of the user"
        ),
        "last_name": fields.String(required=True, description="Last name of the user"),
        "email": fields.String(required=True, description="Email of the user"),
    },
)


@api.route("/")
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, "User successfully created")
    @api.response(400, "Email already registered")
    @api.response(400, "Invalid input data")
    def post(self):
        """Register a new user"""
        user_data = api.payload

        # Simulate email uniqueness check (to be replaced by real validation with persistence)
        existing_user = facade.get_user_by_email(user_data["email"])
        if existing_user:
            return {"error": "Email already registered"}, 400

        new_user = facade.create_user(user_data)
        return {
            "id": new_user.id,
            "first_name": new_user.first_name,
            "last_name": new_user.last_name,
            "email": new_user.email,
        }, 201

    def get(self):
        """
        Retrieve all users.
        """
        users = facade.get_all_users()
        return [
            {
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
            }
            for user in users
        ], 200


@api.route("/<user_id>")
class UserResource(Resource):
    @api.response(200, "User details retrieved successfully")
    @api.response(404, "User not found")
    def get(self, user_id):
        """Get user details by ID"""
        user = facade.get_user(user_id)
        if not user:
            return {"error": "User not found"}, 404
        return {
            "id": str(user.id),
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
        }, 200

    @api.expect(user_model)
    @api.response(200, "User details retrieved successfully")
    @api.response(404, "User not found")
    @api.response(400, "Invalid input data")
    def put(self, user_id):
        """
        Update an existing user.
        """
        user_data = api.payload

        try:
            updated_user = facade.update_user(user_id, user_data)
        except ValueError as error:
            # return {"error": "Invalid input data"}
            return {"error": str(error)}, 400  # Include HTTP 400 Bad Request

        if not updated_user:
            return {"error": "User not found"}, 404
        return {"id": user_id}, 200
