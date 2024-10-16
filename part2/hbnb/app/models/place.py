from models.BaseModel import BaseModel
from models.user import User
from models.amenity import Amenity
from models.review import Review

class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        self.title = self.validate_title(title)
        self.description = description
        self.price = self.validate_price(price)
        self.latitude = self.validate_latitude(latitude)
        self.longitude = self.validate_longitude(longitude)
        self.owner = self.validate_owner(owner)
        self.reviews = []  # List to store related reviews
        self.amenities = []  # List to store related amenities

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

    def validate_owner(self, owner):
        if not isinstance(owner, User):
            raise ValueError("owns the place. This should be validated to ensure the owner exists.")
        return owner

    def update(self, data):
        if 'price' in data:
            self.price = self.validate_price(data['price'])
        if 'latitude' in data:
            self.latitude = self.validate_latitude(data['latitude'])
        if 'longitude' in data:
            self.longitude = self.validate_longitude(data['longitude'])
        super().update(data)