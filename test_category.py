import pytest
from uuid import UUID

from category import Category

class TestCategory():
    def test_name_is_required(self):
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'name'"):
            Category()

    def test_name_must_be_a_string(self):
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'name'"):
            Category()

    def test_name_must_be_less_than_255_characters(self):
        with pytest.raises(ValueError):
            Category("a" * 256)
            
    def test_description_is_optional(self):
        category = Category("Test Category")
        assert  category.description == ""
        assert isinstance(category.id,  UUID)

    def test_is_active_is_optional(self):
        category = Category("Test Category")
        assert category.is_active == True

    def test_is_active_defaults_to_true(self):
        category = Category("Test Category")
        assert category.is_active == True

    def test_is_active_can_be_set_to_false(self):
        category = Category("Test Category", is_active=False)
        assert category.is_active == False

    def test_is_active_can_be_set_to_true(self):
        category = Category("Test Category", is_active=True)
        assert category.is_active == True

    def test_create_category_default_values(self):
        category = Category("Test Category", description="",is_active=True)
        
        assert category.name == "Test Category"
        assert category.description == ""
        assert category.is_active == True

