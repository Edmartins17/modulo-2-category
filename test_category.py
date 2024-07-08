import pytest
from uuid import UUID

from category import Category

class TestCategory():
    def test_name_must_be_a_string_required(self):
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'name'"):
            Category()

    def test_name_must_be_less_than_255_characters(self):
        with pytest.raises(ValueError):
            Category("a" * 256)
            
    def test_description_is_optional(self):
        category = Category(name="Test Category")
        assert  category.description == ""
        assert isinstance(category.id,  UUID)

    def test_is_active_defaults_to_true(self):
        category = Category(name="Test Category")
        assert category.is_active == True

    def test_is_active_can_be_set_to_false(self):
        category = Category(name="Test Category", is_active=False)
        assert category.is_active == False

    def test_is_active_can_be_set_to_true(self):
        category = Category(name="Test Category", is_active=True)
        assert category.is_active == True

    def test_create_category_default_values(self):
        category = Category(name="Test Category", description="",is_active=True)
        
        assert category.name == "Test Category"
        assert category.description == ""
        assert category.is_active == True
class TestUpdateCategory:
    def test_update_category(self):
        category = Category(name="Test Category", description="Updated Description")
        assert category.description == "Updated Description"

    def test_cannot_update_category_with_empty_name(self):
        with pytest.raises(ValueError, match="Name cannot be empty"):
            Category(name="")

class TestActiveCategory:
    def test_activate_inativate_category(self):
        category = Category(name="Test Category", is_active=False)
        category.activate()
        assert category.is_active == True
    def test_active_active_category(self):
        category = Category(name="Test Category", is_active=True)
        category.activate()
        assert category.is_active == True