import sys
import os
import pytest

# Добавляем корень проекта в sys.path, чтобы pytest видел src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.product import Product, Smartphone, LawnGrass
from src.category import Category


def test_smartphone_creation():
    """Тест создания объекта Smartphone"""
    phone = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        "высокая",
        "S23 Ultra",
        "256GB",
        "серый"
    )
    assert phone.name == "Samsung Galaxy S23 Ultra"
    assert phone.price == 180000.0
    assert phone.quantity == 5
    assert phone.efficiency == "высокая"
    assert phone.model == "S23 Ultra"
    assert phone.memory == "256GB"
    assert phone.color == "серый"


def test_lawn_grass_creation():
    """Тест создания объекта LawnGrass"""
    grass = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        10,
        "Россия",
        "7 дней",
        "зеленый"
    )
    assert grass.name == "Газонная трава"
    assert grass.price == 500.0
    assert grass.quantity == 10
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "зеленый"


def test_product_str():
    """Тест строкового представления продукта"""
    product = Product("Test", "Test description", 100.0, 5)
    assert str(product) == "Test, 100.0 руб. Остаток: 5 шт."


def test_category_str():
    """Тест строкового представления категории"""
    product1 = Product("P1", "Desc1", 100.0, 2)
    product2 = Product("P2", "Desc2", 200.0, 3)
    category = Category("Test", "Test desc", [product1, product2])
    # Строка должна точно совпадать с тем, что возвращает Category.__str__
    assert str(category) == "Test, количество продуктов: 5 шт."


def test_category_add_product():
    """Тест добавления продукта в категорию"""
    product = Product("P1", "Desc1", 100.0, 2)
    category = Category("Test", "Test desc", [])
    category.add_product(product)
    # Проверяем, что объект продукта реально лежит в списке (у тебя там список объектов)
    assert str(product) in category.products


def test_category_add_invalid_product():
    """Тест: добавление не-продукта вызывает TypeError"""
    category = Category("Test", "Test desc", [])
    with pytest.raises(TypeError):
        category.add_product("Я просто строка, я не продукт")


def test_smartphone_addition():
    """Тест сложения двух смартфонов"""
    phone1 = Smartphone("S1", "Desc1", 100.0, 5, "High", "M1", "256GB", "Black")
    phone2 = Smartphone("S2", "Desc2", 200.0, 3, "High", "M2", "512GB", "White")
    result = phone1 + phone2
    assert result.price == 300.0
    assert result.quantity == 8
    assert isinstance(result, Smartphone)


def test_lawn_grass_addition():
    """Тест сложения двух газонных трав"""
    grass1 = LawnGrass("G1", "Desc1", 10.0, 10, "RU", "7d", "Green")
    grass2 = LawnGrass("G2", "Desc2", 20.0, 5, "US", "10d", "Green")
    result = grass1 + grass2
    assert result.price == 30.0
    assert result.quantity == 15
    assert isinstance(result, LawnGrass)


def test_different_classes_addition_error():
    """Тест: сложение смартфона и газонной травы вызывает TypeError"""
    phone = Smartphone("S1", "Desc1", 100.0, 5, "High", "M1", "256GB", "Black")
    grass = LawnGrass("G1", "Desc1", 10.0, 10, "RU", "7d", "Green")
    with pytest.raises(TypeError):
        phone + grass


def test_category_iteration():
    """Тест итерации по категории"""
    product1 = Product("P1", "Desc1", 100.0, 2)
    product2 = Product("P2", "Desc2", 200.0, 3)
    category = Category("Test", "Test desc", [product1, product2])
    products_list = list(category)
    assert len(products_list) == 2
    assert products_list[0] is product1
    assert products_list[1] is product2
