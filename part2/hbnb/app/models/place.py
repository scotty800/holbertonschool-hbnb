from ..models.base_models import BaseModel
from app.models.amenity import Amenity
from app.models.review import Review
import uuid
from app.models.user import User

class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner_id):
        super().__init__() 
        self.title = self.validate_title(title)
        self.description = description
        self.price = self.validate_price(price)
        self.latitude = self.validate_latitude(latitude)
        self.longitude = self.validate_longitude(longitude)
        self.owner_id = self.validate_owner(owner_id)   # Validate if owner is provided as a User object
        self.reviews = []  # List to store related reviews
        self.amenities = [] # List to store related amenities

    def to_dict(self):
        """Convert the object to a dictionary for JSON serialization."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "owner_id": self.owner_id,
            "reviews": [review.to_dict() for review in self.reviews],
            "amenities": [amenity.to_dict() for amenity in self.amenities]
        }
    
    def validate_title(self, title):
        if not title or not isinstance(title, str) or len(title) > 100:
            raise ValueError("The title of the place. Required, maximum length of 100 characters.")
        return title

    def add_review(self, review):
        """Add a review to the place."""
        if not isinstance(review, Review):
            raise ValueError("the review have to be an instance valid to review")
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        if not isinstance(amenity, Amenity):
            raise ValueError("that not an instance valide by amenity")
        self.amenities.append(amenity)

    def validate_price(self, price):
        if price <= 0:
            raise ValueError("The price per night for the place. Must be a positive value.")
        return price

    def validate_latitude(self, latitude):
        if not (-90.0 <= latitude <= 90.0):
            raise ValueError("Latitude coordinate for the place location. Must be within the range of -90.0 to 90.0.")
        return latitude

    def validate_longitude(self, longitude):
        if not (-180.0 <= longitude <= 180.0):
            raise ValueError("Longitude coordinate for the place location. Must be within the range of -180.0 to 180.0.")
        return longitude
    
    @staticmethod
    def validate_owner(owner):
        if not isinstance(owner, User):
            raise ValueError("Owner must be an instance of User.")
        return owner.id

    def update(self, data: dict) -> 'Place':
        for field in ['title', 'description', 'price', 'latitude', 'longitude']:
            if field in data:
                if field == 'title':
                    self.title = self.validate_title(data[field])
            elif field == 'description':
                self.description = data[field]  # No validation needed
            elif field == 'price':
                self.price = self.validate_price(data[field])
            elif field == 'latitude':
                self.latitude = self.validate_latitude(data[field])
            elif field == 'longitude':
                self.longitude = self.validate_longitude(data[field])
            return self