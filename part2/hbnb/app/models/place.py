from ..models.base_models import BaseModel
from app.models.amenity import Amenity
from app.models.review import Review
from app.persistence.repository import InMemoryRepository

class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner_id, amenities=None):
        super().__init__()
        self.title = self.validate_title(title)
        self.description = description
        self.price = self.validate_price(price)
        self.latitude = self.validate_latitude(latitude)
        self.longitude = self.validate_longitude(longitude)
        self.user_repo = InMemoryRepository()
        if not isinstance(owner_id, str):
            raise ValueError("The owner ID must be provided and must be a string.")
        
        owner = self.user_repo.get(owner_id)
        if not owner:
            raise ValueError("Propriétaire avec l'ID fourni introuvable.")
        
        self.owner_id = owner_id   # Validate if owner is provided as a User object
        self.reviews = []  # List to store related reviews
        self.amenities = amenities if amenities is not None else []  # List to store related amenities

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

    """def validate_owner(self, owner):
        from user import User
        if not isinstance(owner, User):
            raise ValueError("owns the place. This should be validated to ensure the owner exists.")
        return owner"""

    def update(self, data):
        from app.persistence.repository import InMemoryRepository
        self.user_repo = InMemoryRepository()
        if 'title' in data:
            self.title = self.validate_title(data['title'])
        if 'description' in data:
            self.description = data['description']  # La description peut être mise à jour sans validation supplémentaire
        if 'price' in data:
            self.price = self.validate_price(data['price'])
        if 'latitude' in data:
            self.latitude = self.validate_latitude(data['latitude'])
        if 'longitude' in data:
            self.longitude = self.validate_longitude(data['longitude'])
        if 'owner_id' in data:
            # Vérifier l'existence du propriétaire avant de mettre à jour
            owner = self.user_repo.get(data['owner_id'])
            if owner:
                self.owner_id = owner.id
            else:
                raise ValueError("Propriétaire avec l'ID fourni introuvable.")
        super().update(data)

    def __repr__(self):
        return f"Place(title={self.title}, description={self.description}, price={self.price}, owner_id={self.owner_id})"