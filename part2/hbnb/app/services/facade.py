from app.persistence.repository import InMemoryRepository
import uuid 

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
        return users

    def update_user(self, user_id, user_data):
        user = self.get_user(user_id)
        if not user:
            raise ValueError("User not found")
        self.user_repo.update(user_id, user_data)
        print("DEBUG: User updated successfully")
        updated_user = self.get_user(user_id)
        return updated_user
    
    def validate_request_data(self, data):
        if 'name' not in data or not data['name']:
            raise ValueError("The new name is required.")
        if len(data['name']) > 50:
            raise ValueError("The equipment name cannot exceed 50 characters.")

    def create_amenity(self, amenity_data):
        from app.models.amenity import Amenity
        self.validate_request_data(amenity_data)
        amenity = Amenity(**amenity_data) 
        self.amenity_repo.add(amenity)
        return amenity.to_dict()

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)
    
    def get_all_amenities(self):
        return list(self.amenity_repo.get_all())

    def update_amenity(self, amenity_id, amenity_data):
        self.validate_request_data(amenity_data)
        amenity = self.get_amenity(amenity_id)
        
        if 'name' in amenity_data:
            amenity.name = amenity_data['name']
            self.amenity_repo.update(amenity, amenity_data)
            return amenity.to_dict()
    ".............................................................................."
    def create_place(self, place_data):
        from app.models.place import Place
        from app.models.user import User

        print(f"DEBUG: Received place_data: {place_data}")
        self.validate_place_data(place_data)

        owner_id = place_data.get('owner_id')
        print(f"DEBUG: Attempting to retrieve user with ID: {owner_id}")
        user = self.get_user(owner_id)
        if user is None:
            print(f"DEBUG: User not found with ID façade: {owner_id}")
            raise ValueError(f"User with ID {owner_id} not found.")
        place_data['owner_id'] = user['id']
        
        amenities_list = place_data.get('amenities', [])
        valid_amenities = []
        if isinstance(amenities_list, list):
            for amenity_id in amenities_list:
                amenity = self.amenity_repo.get(amenity_id)
                if amenity is not None:
                    valid_amenities.append(amenity)
                else:
                    print(f"DEBUG: Amenity not found with ID: {amenity_id}")
                    raise ValueError(f"Amenity with ID {amenity_id} not found.")
        else:
            print("DEBUG: Amenities list is not a valid list.")
            place_data['amenities'] = valid_amenities
            place_id = str(uuid.uuid4())
            place = Place(id=place_id, **place_data)
            self.place_repo.add(place)
            place_dict = place.to_dict()
            print(f"DEBUG: Place dictionary before JSON serialization: {place_dict}")
            return place_dict
    
    def validate_place_data(self, price, latitude, longitude, owner_id):
        if not isinstance(price, float):
            try:
                price = float(price)
            except ValueError:
                raise ValueError("Error: Price should be a valid float value.")
        if price < 0:
            raise ValueError("Error: Price should be a non-negative float.")
        if not (-90 <= latitude <= 90):
            raise ValueError("Error: Latitude should be between -90 and 90.")
        if not (-180 <= longitude <= 180):
            raise ValueError("Error: Longitude should be between -180 and 180.")
        if owner_id is None or not isinstance(owner_id, str):
            raise ValueError("Error: The owner ID must be provided and must be a string.")
        
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