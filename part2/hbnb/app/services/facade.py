from app.persistence.repository import InMemoryRepository
from ..models.user import User
from ..models.amenity import Amenity
from ..models.place import Place
import uuid

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()
        self.users = []
        self.places = []
        self.owners = []
        
    def create_user(self, user_data):
        user = User(**user_data, id=str(uuid.uuid4()))
        if user.is_owner:
            self.owners.append(user)
            print(f"DEBUG: user is owner: {user}")
        else:
            print(f"DEBUG: user is client: {user}")
            self.users.append(user)
            
        self.user_repo.add(user)
        return user
    
    def get_user(self, user_id):
        print(f"DEBUG: Attempting to get user with ID façade: {user_id}")
        user = self.user_repo.get(user_id)
        return user
    
    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)
    
    def get_all_users(self):
        print(f"DEBUG: get all USER: {self}")
        return list(self.user_repo.get_all())
    
    def update_user(self, user_id, user_data):
        user = self.get_user(user_id)
        updated_user = User.update(user, user_data)
        return updated_user
    
    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        print(f"DEBUG: user amenity add: {amenity}")
        self.amenity_repo.add(amenity)
        return amenity.to_dict()

    def get_amenity(self, amenity_id):
        print(f"DEBUG: save amenity_id : {amenity_id}")
        return self.amenity_repo.get(amenity_id)
    
    def get_all_amenities(self):
        list(self.amenity_repo.get_all())
    
    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.get_amenity(amenity_id)
        update_amenity = Amenity.update(amenity, amenity_data)
        return update_amenity

    
    def create_place(self, place_data):
        self.validate_place_data(place_data)
        owner_id = place_data.get('owner_id')
        print(f"not retrieve owner with ID: {owner_id}")
        
        owner = self.get_user(owner_id)
        if not owner or not owner.is_owner:
            raise PermissionError("You do not have permission to create a place.")
        
        new_place = Place(**place_data, id=str(uuid.uuid4()))
        self.place_repo.add(new_place)
        self.places.append(new_place)
        return new_place
    
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
        if place is None:
            raise ValueError("Place not found")
        return place.to_dict()
    
    def get_all_places(self):
        place = self.place_repo.get_all()
        return [place.to_dict() for place in place]
    
    def update_place(self, place_id, place_data):
        place = self.get_place(place_id)
        for key, value in place_data.items():
            setattr(place, key, value) 
        self.place_repo.update(place_id, place)  
        return place