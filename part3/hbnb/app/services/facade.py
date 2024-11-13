from ..models.user import User
from ..models.amenity import Amenity
from ..models.place import Place
from ..models.review import Review
from app.persistence.repository import SQLAlchemyRepository

class HBnBFacade:
    def __init__(self):
        self.user_repo = SQLAlchemyRepository(User)
        self.place_repo = SQLAlchemyRepository(Place)
        self.review_repo = SQLAlchemyRepository(Review)
        self.amenity_repo = SQLAlchemyRepository(Amenity)

    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user_by_id(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    def get_all_users(self):
        return list(self.user_repo.get_all())

    def update_user(self, user_id, user_data):
        user = self.get_user_by_id(user_id)
        if user:
            for key, value in user_data.items():
                setattr(user, key, value)
            self.user_repo.update(user_id, user)
        return user

    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return list(self.amenity_repo.get_all())

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.get_amenity(amenity_id)
        if amenity:
            for key, value in amenity_data.items():
                setattr(amenity, key, value)
            self.amenity_repo.update(amenity_id, amenity)
        return amenity

    def create_place(self, place_data):
        self.validate_place_data(place_data)
        owner_id = place_data.get('owner_id')
        owner = self.get_user_by_id(owner_id)
        if not owner or not owner.is_owner:
            raise PermissionError("You do not have permission to create a place.")

        place = Place(**place_data)
        self.place_repo.add(place)
        return place

    def validate_place_data(self, place_data):
        required_fields = ['title', 'description', 'price', 'latitude', 'longitude']
        for field in required_fields:
            if field not in place_data:
                raise ValueError(f"The field '{field}' is required to create a place.")

        if place_data['price'] <= 0:
            raise ValueError("The price must be a positive number.")
        if not (-90 <= place_data['latitude'] <= 90):
            raise ValueError("Latitude must be within the range of -90 to 90.")
        if not (-180 <= place_data['longitude'] <= 180):
            raise ValueError("Longitude must be within the range of -180 to 180.")

    def get_place(self, place_id):
        place = self.place_repo.get(place_id)
        if not place:
            raise ValueError("Place not found")
        return place

    def get_all_places(self):
        return list(self.place_repo.get_all())

    def update_place(self, place_id, place_data):
        place = self.get_place(place_id)
        if place:
            for key, value in place_data.items():
                setattr(place, key, value)
            self.place_repo.update(place_id, place)
        return place

    def create_review(self, review_data):
        review = Review(**review_data)
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return list(self.review_repo.get_all())

    def update_review(self, review_id, review_data):
        review = self.get_review(review_id)
        if review:
            for key, value in review_data.items():
                setattr(review, key, value)
            self.review_repo.update(review_id, review)
        return review

    def delete_review(self, review_id):
        return self.review_repo.delete(review_id)
