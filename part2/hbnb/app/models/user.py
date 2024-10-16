import re
from base_models import BaseModel

class User(BaseModel):
    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin

        if len(first_name) > 50:
            raise ValueError("First name should not exceed 50 characters")
        if len(last_name) > 50:
            raise ValueError ("First name should not exceed 50 characters")
        if not self.is_valid_email(email):
            raise ValueError("Invalid email format")

    def is_valid_email(self, email):
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(email_regex, email) is not None