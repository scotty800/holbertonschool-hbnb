"""_summary_"""

from app.persistence.repository import InMemoryRepository


class HBnBFacade:
    """
    HBnBFacade provides a simplified interface to interact with
    multiple repositories, including user, place, review, and amenity repositories.

    Attributes:
        user_repo (InMemoryRepository): Repository for user data.
        place_repo (InMemoryRepository): Repository for place data.
        review_repo (InMemoryRepository): Repository for review data.
        amenity_repo (InMemoryRepository): Repository for amenity data.
    """

    def __init__(self):
        """
        Initializes the HBnBFacade with instances
        of InMemoryRepository for users, places, reviews, and amenities.
        """
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    def create_user(self, user_data):
        """
        Placeholder method for creating a user.

        Args:
            user_data (dict): A dictionary containing user information.

        Returns:
            None
        """
        pass

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute("email", email)

    def get_place(self, place_id):
        """
        Placeholder method for fetching a place by its ID.

        Args:
            place_id (int): The ID of the place to retrieve.

        Returns:
            None
        """
        pass


def create_amenity(self, amenity_data):
    """
    Creates a new amenity and stores it in the repository.

    Args:
        amenity_data (dict): A dictionary containing amenity information (e.g., 'name').

    Raises:
        ValueError: If the 'name' field is missing or empty, or if name length exceeds 50 characters.

    Returns:
        Amenity: The created Amenity object.
    """
    # Validate that the 'name' field is present and not empty
    if "name" not in amenity_data or not amenity_data["name"]:
        raise ValueError("Amenity name is required.")

    # Validate that the name does not exceed 50 characters
    if len(amenity_data["name"]) > 50:
        raise ValueError("Amenity name cannot exceed 50 characters.")

    # Create the Amenity object
    new_amenity = Amenity(name=amenity_data["name"])
    new_amenity.id = self.amenity_id_counter  # Simulate ID assignment

    # Add the new amenity to the repository
    self.amenities.append(new_amenity)
    self.amenity_id_counter += 1

    return new_amenity


def get_amenity(self, amenity_id):
    """
    Retrieves an amenity by its ID.

    Args:
        amenity_id (int): The ID of the amenity to retrieve.

    Returns:
        Amenity: The found Amenity object or None if not found.
    """
    for amenity in self.amenities:
        if amenity.id == amenity_id:
            return amenity
    return None


def get_all_amenities(self):
    """
    Retrieves all amenities in the repository.

    Returns:
        list: A list of all Amenity objects.
    """
    return self.amenities


def update_amenity(self, amenity_id, amenity_data):
    """
    Updates an existing amenity's information.

    Args:
        amenity_id (int): The ID of the amenity to update.
        amenity_data (dict): A dictionary containing the updated amenity information.

    Raises:
        ValueError: If the 'name' field is missing or empty, or if name length exceeds 50 characters.

    Returns:
        Amenity: The updated Amenity object, or None if the amenity is not found.
    """
    # Find the amenity by ID
    amenity = self.get_amenity(amenity_id)
    if not amenity:
        return None

    # Validate that the 'name' field is present and not empty
    if "name" not in amenity_data or not amenity_data["name"]:
        raise ValueError("Amenity name is required.")

    # Validate that the name does not exceed 50 characters
    if len(amenity_data["name"]) > 50:
        raise ValueError("Amenity name cannot exceed 50 characters.")

    # Update the amenity's name
    amenity.name = amenity_data["name"]
    return amenity
