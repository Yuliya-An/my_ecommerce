import pytest
from src.main import Product, Category


def test_product_creation():
    """Проверка создания товара и его атрибутов."""
    p = Product("Тест", "Описание", 100.0, 10)
    assert p.name == "Тест"
    assert p.price == 100.0
    assert p.quantity == 10


def test_product_count():
    """Проверка счетчика товаров."""
    # Сбрасываем счетчик для чистоты теста
    Product.product_count = 0
    Product("Товар 1", "Описание", 10.0, 1)
    Product("Товар 2", "Описание", 20.0, 2)
    assert Product.product_count == 2


def test_category_creation():
    """Проверка создания категории."""
    c = Category("Электроника", "Описание категории")
    assert c.name == "Электроника"
    assert c.products == []


def test_add_product_to_category():
    """Проверка добавления товара в категорию."""
    p = Product("Мышка", "Описание", 500.0, 1)
    c = Category("Периферия", "Описание")
    c.add_product(p)
    assert len(c.products) == 1
    assert c.products[0].name == "Мышка"


def test_category_count():
    """Проверка счетчика категорий."""
    Category.category_count = 0
    Category("Кат 1", "Описание")
    Category("Кат 2", "Описание")
    assert Category.category_count == 2
