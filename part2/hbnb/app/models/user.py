import re
from .base_models import BaseModel
import uuid

class User(BaseModel):
    def __init__(self, first_name, last_name, email, is_admin=False, is_owner=False):
        super().__init__()

        if len(first_name) > 50:
            raise ValueError("First name should not exceed 50 characters")
        if len(last_name) > 50:
            raise ValueError("Last name should not exceed 50 characters")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("The email address is invalid")

        self.id = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.is_owner = is_owner

    def to_dict(self):
        """Convert the object to a dictionary for JSON serialization."""
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "is_admin": self.is_admin,
            "is_owner": self.is_owner
        }

    def update(self, data):
        if not isinstance(data, dict):
            raise ValueError("Expected a dictionary for update")
        if 'first_name' in data:
            if len(data['first_name']) > 50:
                raise ValueError("First name should not exceed 50 characters")
            self.first_name = data['first_name']
        if 'last_name' in data:
            if len(data['last_name']) > 50:
                raise ValueError("Last name should not exceed 50 characters")
            self.last_name = data['last_name']

        if 'email' in data:
            if not re.match(r"[^@]+@[^@]+\.[^@]+", data['email']):
                raise ValueError("The email address is invalid")
            self.email = data['email']
        if 'is_owner' in data:
            self.is_owner = data['is_owner']

    def __str__(self):
        return f"User({self.first_name} {self.last_name}, Email: {self.email}, Admin: {self.is_admin})"

    def __repr__(self):
        return f"User(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, email={self.email}, is_admin={self.is_admin})"