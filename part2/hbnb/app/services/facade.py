from app.persistence.repository import InMemoryRepository
from app.models.review import Review

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    def create_user(self, user_data):
        from app.models.user import User
        user = User(**user_data)
        self.user_repo.add(user)
        return user.to_dict()

    def get_user(self, user_id):
        print(f"DEBUG: Attempting to get user with ID façade: {user_id}")
        user = self.user_repo.get(user_id)
        if user:
            print(f"DEBUG: User found: {user.to_dict()} get user")
            user_dict = user.to_dict()
            print(f"DEBUG: User found : {user_dict} get user")
            print(f"DEBUG: User dict type: {type(user_dict)}")
            return user_dict
        else:
            print(f"DEBUG: No user found with ID: {user_id}")
            return None

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    def get_all_user(self):
        users = self.user_repo.get_all()
        return [user.to_dict() for user in users]

    def update_user(self, user_id, user_data):
        user = self.get_user(user_id)
        if not user:
            raise ValueError("User not found")

        user.update(user_data)  # Appelle la méthode update de User
        self.user_repo.update(user)  # Enregistre l'instance mise à jour dans le dépôt

        print("DEBUG: User updated successfully")
        updated_user = self.get_user(user_id)
        return updated_user

    def create_review(self, review_data):
        review = Review(**review_data)
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return list(self.review_repo.get_all())

    def get_reviews_by_place(self, place_id):
        all_reviews = self.review_repo.get_all()

    def update_review(self, review_id, review_data):
        review = self.get_review(review_id)

        if not review:
            raise ValueError('Review not found')

        if 'text' in review_data:
            review.text = review_data['text']
        if 'rating' in review_data:
            review.rating = review_data['rating']

        self.review_repo.update(review_id, review_data)
        return review

    def delete_review(self, review_id):
        return self.review_repo.delete(review_id)