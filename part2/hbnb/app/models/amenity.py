"""
This module defines the Amenity class, which represents amenities or equipment 
in a broader system. The class inherits from BaseModel, and each amenity has 
a name with a maximum length constraint.
"""

from .base_models import BaseModel

class Amenity(BaseModel):
    """
    Amenity - Represents an equipment or amenity in the system
    
    Inherits from BaseModel and adds a name attribute. The name is constrained 
    to a maximum length of 50 characters.
    
    Attributes:
    - name: A string representing the name of the amenity (must be <= 50 chars)
    
    Methods:
    __init__: Initializes the Amenity instance with a name and validates its length.
    """

    def __init__(self, name):
        """
        __init__ - Initializes an Amenity object with a name attribute
        
        @arg: name - The name of the amenity (cannot exceed 50 characters)
        
        Raises:
        - ValueError: If the length of the name exceeds 50 characters
        """
        super().__init__()
        self.name = name

        if len(name) > 50:
            raise ValueError("The equipment name cannot exceed 50 characters.")
