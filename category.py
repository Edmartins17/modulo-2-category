from dataclasses import dataclass, field
import uuid

@dataclass
class Category:
    name: str
    description: str = ""  
    is_active: bool = True
    id: uuid.UUID = field(default_factory=uuid.uuid4)

    def __post_init__(self):
        self.validate()
            
    def __str__(self):
        return f"{self.name} - {self.description} - {self.is_active}"
    def __repr__(self):
        return f"{self.name} - {self.description} - {self.is_active}"
    
    def __eq__(self, value: object):
        if not isinstance(value, Category):
            return False
        return self.id == value.id
    
    def update_category(self, name, description):
        self.name = name
        self.description = description
        self.validate()
        
    def activate(self):
        self.is_active = True

        self.validate()

    def deactivate(self):
        self.is_active = False

        self.validate()
    
    def validate(self):
        if not self.name:
            raise ValueError("Name cannot be empty")
        if len(self.name) > 255:
            raise ValueError("Name must be less than 255 characters")
        