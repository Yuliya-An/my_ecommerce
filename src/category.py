from typing import List
from src.product import Product


class Category:
    # Классовые атрибуты (те самые, которые требовал куратор)
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: List[Product] | None = None):
        self.name = name
        self.description = description
        # Сохраняем твою приватность __products
        self.__products = products if products is not None else []

        # Локальный счетчик товаров в этой категории
        self.product_count = 0

        # Увеличиваем глобальный счетчик категорий
        Category.category_count += 1

        # Если список товаров передан при создании, добавляем их через метод add_product
        if products:
            for product in products:
                self.add_product(product)

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("В категорию можно добавлять только объекты класса Product")

        self.__products.append(product)
        self.product_count += 1  # Увеличиваем локальный счетчик
        Category.product_count += 1  # Увеличиваем глобальный счетчик класса

    @property
    def products(self) -> str:
        # Сохраняем твой красивый формат вывода товаров
        res = []
        for p in self.__products:
            res.append(f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт.")
        return "\n".join(res)

    def __iter__(self):
        return iter(self.__products)

    def __repr__(self) -> str:
        return f"Category(name={self.name}, products_count={self.product_count})"