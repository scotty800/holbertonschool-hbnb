from .base_models import BaseModel

class Amenity(BaseModel):
    def _init_(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name

        if len(name) > 50:
            raise ValueError("The equipment name cannot exceed 50 characters.")
        
    def update(self, new_name):
        if not new_name:
            raise ValueError("The new name is required.")
        if len(new_name) > 50:
            raise ValueError("The new name cannot exceed 50 characters.")
        
        self.name = new_name
        return self


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
            }
