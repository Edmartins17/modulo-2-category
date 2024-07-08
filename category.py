import uuid

class Category:
    def __init__(
            self,
            name,
            id = "",
            description = "",
            is_active = True,
    ):
        self.id = id or uuid.uuid4()
        self.name = name
        self.description = description
        self.is_active = is_active

        self.validate()
        
    def __str__(self):
        return f"{self.name} - {self.description} - {self.is_active}"
    def __repr__(self):
        return f"{self.name} - {self.description} - {self.is_active}"
    def update_category(self, name, description):
        self.name = name
        self.description = description
        self.validate(self)
        
    def validate(self):
        if not self.name:
            raise TypeError("Name cannot be empty")
        if len(self.name) > 255:
            raise ValueError("Name must be less than 255 characters")
        