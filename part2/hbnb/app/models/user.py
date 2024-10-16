from models.BaseModel import BaseModel
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

    def format_email(self, email):
        if not isinstance(email, str):
            raise ValueError ("Invalid email format")

    def is_valide_email(self, email):
        if '@' in email and "." in email.split('@')[-1]:
            return True
        return False