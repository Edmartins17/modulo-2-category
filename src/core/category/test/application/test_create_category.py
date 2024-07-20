from unittest.mock import MagicMock
from uuid import UUID

import pytest
from src.core.category.application.create_category import CreateCategoryRequest, InvalidCategoryData, create_category
from src.core.category.domain.category import Category
from src.core.category.domain.category_repository import CategoryRepository


class TestCreateCategory:
    def test_create_category_with_data_valid(self):
        category = create_category(
            repository=MagicMock(CategoryRepository)
        )
        assert category is not None
        assert isinstance(category, create_category)

    def test_create_category_with_empty_name(self):
        with pytest.raises(InvalidCategoryData, match="Name cannot be empty") as ex_info:
            request = CreateCategoryRequest(
                name="",
                description="Test Description",
                is_activated=True
            )
            useCreateCategory = create_category(
                repository=MagicMock(CategoryRepository)
            )
            useCreateCategory.execute(request)

        assert ex_info.type == InvalidCategoryData
        assert "Name cannot be empty" in str(ex_info.value)