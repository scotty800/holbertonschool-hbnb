from flask import request, jsonify
from app import db
from models.user import User
from flask import request, jsonify
from app import create_app, db
from models.user import User

app = create_app()

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
