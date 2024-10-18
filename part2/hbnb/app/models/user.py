import re
from .base_models import BaseModel

class User(BaseModel):
    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()

        if len(first_name) > 50:
            raise ValueError("First name should not exceed 50 characters")
        if len(last_name) > 50:
            raise ValueError ("First name should not exceed 50 characters")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("The email address is invalid")

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin

    def update(self, data):
        if 'first_name' in data:
            self.first_name = data['first_name']
        if 'last_name' in data:
            self.last_name = data['last_name']
        if 'email' in data and re.match(r"[^@]+@[^@]+\.[^@]+", data['email']):
            self.email = data['email']
        super().update(data)