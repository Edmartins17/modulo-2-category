import pytest
import unittest

from category import Category

class TestCategory(unittest.TestCase):
    def test_name_is_required(self):
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'name'"):
            Category()
    def test_name_must_be_a_string(self):
        with self.assertRaisesRegex(TypeError, "missing 1 required positional argument: 'name'"):
            Category()
    def test_name_must_be_less_than_255_characters(self):
        with self.assertRaises(ValueError):
            Category("a" * 256)
    def test_description_is_optional(self):
        category = Category("Test Category")
        self.assertEqual(category.description, "")
    def test_is_active_is_optional(self):
        category = Category("Test Category")
        self.assertTrue(category.is_active)
    def test_is_active_defaults_to_true(self):
        category = Category("Test Category")
        self.assertTrue(category.is_active)
    def test_is_active_can_be_set_to_false(self):
        category = Category("Test Category", is_active=False)
        self.assertFalse(category.is_active)
    def test_is_active_can_be_set_to_true(self):
        category = Category("Test Category", is_active=True)
        self.assertTrue(category.is_active)
    def test_create_category_default_values(self):
        category = Category("Test Category", description="",is_active=True)
        self.assertEqual(category.name, "Test Category")
        self.assertEqual(category.description, "")
        self.assertTrue(category.is_active)

        assert category.name == "Test Category"
        assert category.description == ""
        assert category.is_active == True

if __name__ == "__main__":
    unittest.main()
