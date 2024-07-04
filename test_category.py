import unittest

from category import Category

class TestCategory(unittest.TestCase):
    def test_name_is_required(self):
        with self.assertRaises(TypeError):
            Category()
    def test_name_must_be_less_than_255_characters(self):
        with self.assertRaises(ValueError):
            Category("a" * 256)

if __name__ == "__main__":
    unittest.main()
