from app.persistence.repository import InMemoryRepository
from app.models.user import User
import uuid


class HBnBFacade:
    """
    Facade class to provide a simplified interface for user, place, review, and amenity operations.
    Ensures a single instance is used throughout the application (Singleton pattern).
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        Ensures only one instance of HBnBFacade is created (Singleton pattern).

        Returns:
            HBnBFacade: The single instance of the HBnBFacade class.
        """
        if cls._instance is None:
            cls._instance = super(HBnBFacade, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        """
        Initializes repositories for users, places, reviews, and amenities.
        This initialization happens only once per instance.
        """
        if not hasattr(self, "initialized"):
            self.user_repo = InMemoryRepository()
            self.place_repo = InMemoryRepository()
            self.review_repo = InMemoryRepository()
            self.amenity_repo = InMemoryRepository()

            self.initialized = True

    def create_user(self, user_data):
        """
        Creates a new user and stores it in the user repository.

        Args:
            user_data (dict): Dictionary containing user information like first_name, last_name, and email.

        Returns:
            User: The newly created User object.
        """
        # Placeholder method for creating a user
        user = User(**user_data, id=str(uuid.uuid4()))
        # User.check(user_data)
        User.validate_request_data(user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        """
        Retrieves a user by their unique ID from the user repository.

        Args:
            user_id (str): The unique identifier of the user.

        Returns:
            User: The user object if found, otherwise None.
        """
        return self.user_repo.get(user_id)

    def update_user(self, user_id, user_data):
        """
        Updates an existing user in the repository.

        Args:
            user_id (int): The ID of the user to update.
            user_data (dict): The updated user information.

        Returns:
            User: The updated user object, or None if not found.
        """
        User.validate_request_data(user_data)
        user = self.get_user(user_id)
        if user:
            user.update(user_data)
        return user

    def get_user_by_email(self, email):
        """
        Retrieves a user by their email from the user repository.

        Args:
            email (str): The email address of the user.

        Returns:
            User: The user object if found, otherwise None.
        """
        return self.user_repo.get_by_attribute("email", email)

    def get_all_users(self):
        """
        Retrieves all users from the user repository.

        Returns:
            list: A list of all User objects.
        """
        return (
            self.user_repo.get_all()
        )  # Assuming `get_all` is a method in InMemoryRepository

    def get_place(self, place_id):
        """
        Placeholder method to retrieve a place by its unique ID.
        Logic to be implemented in later tasks.

        Args:
            place_id (str): The unique identifier of the place.

        Returns:
            None: No functionality implemented yet.
        """
        # pass


facade = HBnBFacade()
