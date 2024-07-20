
from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category_repository import InMemoryCategoryRepository


class TestInMemoryCategoryRepository:
    def test_save_category(self):
        category_repository = InMemoryCategoryRepository()
        category = Category(name="Test Category", description="Test Description")
        category_repository.save(category)

        assert len(category_repository.categories) == 1
        assert category_repository.categories[0] == category