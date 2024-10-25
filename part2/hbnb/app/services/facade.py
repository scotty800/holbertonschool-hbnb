from app.persistence.repository import InMemoryRepository
import logging


class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    def create_user(self, user_data):
        logging.info(f"Attempting to create user with data: {user_data}")
        from app.models.user import User

        user = User(**user_data)
        existing_user = self.user_repo.get_by_attribute("email", user.email)
        if existing_user:
            raise ValueError(f"Error: An user with email {user.email} already exists.")
        self.user_repo.add(user)
        logging.info(f"User created successfully: {user}")
        return user

    def get_user(self, user_id):
        logging.info(f"Attempting to retrieve user with ID: {user_id}")
        user = self.user_repo.get(user_id)  # Implémentez cela selon votre logique
        if not user:
            logging.warning(f"User with ID {user_id} not found.")
            raise ValueError("User not found")
        logging.info(f"User retrieved: {user}")  # Log l'utilisateur récupéré
        return user

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute("email", email)

    def get_all_user(self):
        users = self.user_repo.get_all()
        logging.info("All users retrieved from the database.")
        return users

    def update_user(self, user_id, user_data):
        logging.info(
            f"Attempting to update user with ID: {user_id} and data: {user_data}"
        )
        user = self.get_user(user_id)
        if not user:
            logging.error(f"User with ID {user_id} not found.")
            raise ValueError("User not found")
        self.user_repo.update(user_id, user_data)
        logging.info(f"User updated successfully: {user}")
        return user

    def create_place(self, place_data):
        logging.info(f"Attempting to create place with data: {place_data}")

        from app.models.place import Place

        required_keys = ["price", "latitude", "longitude", "owner_id"]
        for key in required_keys:
            if key not in place_data:
                raise ValueError(f"Missing required field: {key}")

        price = place_data["price"]
        latitude = place_data["latitude"]
        longitude = place_data["longitude"]
        owner_id = place_data["owner_id"]

        self.validate_place_data(price, latitude, longitude, owner_id)
        owner = self.user_repo.get(owner_id)
        if not owner:
            logging.error(f"The owner specified with ID '{owner_id}' does not exist.")
            raise ValueError(
                f"Error: The owner specified with ID '{owner_id}' does not exist."
            )
        else:
            logging.info(f"Owner found: {owner}")

        try:
            place = Place(**place_data)
            self.place_repo.add(place, user_id=place_data["owner_id"])
            logging.info(f"Place created successfully: {place}")
            return place
        except Exception as e:
            logging.error(f"Failed to create place: {str(e)}")
            raise ValueError(f"Failed to create place: {str(e)}")

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
            raise ValueError(
                "Error: The owner ID must be provided and must be a string."
            )

    def get_place(self, place_id):
        place = self.place_repo.get(place_id)
        if place is None:
            raise ValueError("Place not found")
        return place

    def get_all_places(self):
        place = self.place_repo.get_all()
        logging.info("All places retrieved from the database.")
        return place

    def update_place(self, place_id, place_data):
        place = self.get_place(place_id)
        for key, value in place_data.items():
            setattr(place, key, value)  # Met à jour les attributs de l'objet
        self.place_repo.update(place_id, place)
        logging.info(f"Place updated successfully: {place}")
        return place
