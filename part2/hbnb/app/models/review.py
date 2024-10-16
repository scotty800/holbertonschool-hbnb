from models.BaseModel import BaseModel
from models.place import Place
from models.user import User
from datetime import datetime

class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        self.text = text
        self.rating = self.validate_rating(rating)
        self.place = self.validate_place(place)
        self.user = self.validate_user(user)

    def validate_rating(self,rating):
        if not (1 <= rating <= 5):
            raise ValueError(" must be between 1 and 5.")
        return rating
    
    def validate_place(self, place):
        if not isinstance(place, Place):
            raise ValueError("Place instance being reviewed. Must be validated to ensure the place exists.")
        return place
    
    def validate_user(self, user):
         if not isinstance(user, User):
            raise ValueError("User instance of who wrote the review. Must be validated to ensure the user exists.")
         return user
    
    def update(self, data):
        if 'rating' in data:
            self.rating = self.validate_rating(data['rating'])
        super().update(data)