from .base_models import BaseModel
from .user import User


class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()

        if len(title) > 100:
            raise ValueError("Title must not exceed 100 characters")
        if price <= 0:
            raise ValueError("Price must be a positive value")
        if not (-90.0 <= latitude <= 90.0):
            raise ValueError("Latitude must be between -90.0 and 90.0")
        if not (-180.0 <= longitude <= 180.0):
            raise ValueError("Longitude must be between -180.0 and 180.0")

        if not isinstance(owner, User):
            raise ValueError("Owner must be a valid User instance")

        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = []
        self.amenities = []

    def add_review(self, review):
        self.reviews.append(review)

    def add_amenity(self, amenity):
        self.amenities.append(amenity)
