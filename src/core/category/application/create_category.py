from dataclasses import dataclass
from uuid import UUID

from src.core.category.application.exceptions import InvalidCategoryData
from src.core.category.domain.category import Category
from src.core.category.domain.category_repository import CategoryRepository

@dataclass
class CreateCategoryRequest:
    name: str
    description: str =""
    is_activated: bool = True

class create_category:
    
    def __init__(self, repository: CategoryRepository):
        self.repository = repository
    
    def execute(self,request: CreateCategoryRequest) -> UUID:
        try:
            category = Category(
                name=request.name,
                description=request.description,
                is_active=request.is_activated
            )
        except ValueError as err:
            raise InvalidCategoryData(err)

        self.repository.save(category)
        return category.id
