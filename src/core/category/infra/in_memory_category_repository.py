from src.core.category.domain.category import Category


class InMemoryCategoryRepository:
    def __init__(self, categories=None):
        self.categories = categories or []

    def save(self, category: Category) -> Category:
        self.categories.append(category)