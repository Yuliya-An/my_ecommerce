from typing import List
from src.product import Product


class Category:
    """
    Класс, представляющий категорию товаров.

    Атрибуты класса:
        category_count (int): Общее количество созданных категорий.
        product_count (int): Общее количество всех товаров во всех категориях.

    Атрибуты экземпляра:
        name (str): Название категории.
        description (str): Описание категории.
        products (List[Product]): Список товаров в категории.
        product_count (int): Количество товаров в данной категории.
    """

    category_count = 0
    product_count = 0  # Глобальный счётчик всех товаров

    def __init__(self, name: str, description: str, products: List[Product] | None = None):
        """
        Инициализация экземпляра категории.

        Args:
            name (str): Название категории.
            description (str): Описание категории.
            products (List[Product] | None): Начальный список товаров (по умолчанию None).
        """
        self.name = name
        self.description = description
        self.products: List[Product] = []
        self.product_count = 0  # Локальный счётчик товаров в этой категории
        Category.category_count += 1

        if products:
            for product in products:
                self.add_product(product)

    def add_product(self, product: Product) -> None:
        """
        Добавляет товар в категорию.

        Args:
            product (Product): Объект товара для добавления.
        """
        self.products.append(product)
        self.product_count += 1      # Увеличиваем локальный счётчик
        Category.product_count += 1  # Увеличиваем глобальный счётчик

    def __repr__(self) -> str:
        """
        Строковое представление объекта.

        Returns:
            str: Информация о категории и количестве товаров.
        """
        return f"Category(name={self.name}, products_count={len(self.products)})"
