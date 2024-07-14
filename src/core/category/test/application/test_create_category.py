from uuid import UUID
from src.core.category.application.create_category import create_category


class TestCreateCategory:
    def test_create_category_with_data_valid(self):
        category_id = create_category(
            name="Test Category",
            description="Test Description",
            is_activated=True
        )
        assert category_id is not None
        assert isinstance(category_id, UUID)
