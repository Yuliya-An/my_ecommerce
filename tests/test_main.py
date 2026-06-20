import sys
import os
import pytest

# Добавляем корень проекта в sys.path, чтобы pytest видел src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.product import Product, Smartphone, LawnGrass
from src.category import Category
# Импортируем то, что у тебя в main_16_1.py (или main.py), если там есть глобальные вещи.
# Если в main.py нет отдельных функций, а только скрипт, то этот импорт можно опустить.
# from src.main import ...  # раскомментируй, если в main есть отдельные функции для теста


def test_smartphone_creation():
    """Тест создания объекта Smartphone — твой стиль проверок"""
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
    """Тест создания объекта LawnGrass — твой стиль"""
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
    """Твой тест строкового представления базового Product"""
    product = Product("Test", "Test description", 100.0, 5)
    assert str(product) == "Test, 100.0 руб. Остаток: 5 шт."


def test_different_classes_addition_error():
    """Твой тест на сложение разных классов — важно для покрытия логики __add__"""
    phone = Smartphone(
        "S1", "Desc1", 100.0, 5, "High", "M1", "256GB",
        "Black"
    )
    grass = LawnGrass(
        "G1", "Desc1", 10.0, 10, "RU", "7d", "Green"
    )
    with pytest.raises(TypeError):
        phone + grass


def test_category_creation_and_counters():
    """Проверяем создание категории и рост total_categories — как в твоём сценарии"""
    initial_total = Category.total_categories
    category = Category("Электроника")
    assert category.name == "Электроника"
    assert Category.total_categories == initial_total + 1
    assert category.product_count == 0


def test_add_valid_product_and_total_products():
    """Добавляем продукт и проверяем рост total_products — часть сценария main.py"""
    initial_total_products = Category.total_products
    product = Product("Мышь", "Беспроводная мышь", 1500.0, 10)
    category = Category("Аксессуары")
    category.add_product(product)
    assert category.product_count == 1
    assert Category.total_products == initial_total_products + 1


def test_add_invalid_product_raises_type_error():
    """Проверка защиты типа в add_product — как в блоке try/except твоего main.py"""
    category = Category("Тестовая категория")
    with pytest.raises(TypeError) as exc_info:
        category.add_product("Я просто строка, я не продукт")
    assert "В категорию можно добавлять только объекты класса Product" in str(exc_info.value)


def test_products_property_returns_correct_string_format():
    """Ключевой тест для main.py: проверяем, что products — это строка без скобок, нужный формат"""
    p1 = Product("Товар 1", "Описание 1", 100.0, 5)
    p2 = Product("Товар 2", "Описание 2", 200.0, 3)
    category = Category("Мои товары")
    category.add_product(p1)
    category.add_product(p2)
    result = category.products
    assert isinstance(result, str)
    assert '[' not in result
    assert ']' not in result
    assert "Товар 1, 100.0 руб. Остаток: 5 шт." in result
    assert "Товар 2, 200.0 руб. Остаток: 3 шт." in result
    assert result.count("\n") == 1


def test_category_iteration():
    """Итерация по категории — как в for product in category твоего main.py"""
    p1 = Product("P1", "Desc1", 100.0, 2)
    p2 = Product("P2", "Desc2", 200.0, 3)
    category = Category("Итерация тест")
    category.add_product(p1)
    category.add_product(p2)
    products_list = list(category)
    assert len(products_list) == 2
    assert products_list[0] is p1
    assert products_list[1] is p2


def test_main_scenario_full_flow():
    """Полный мини-сценарий как в main.py: категории, 2 травы, вывод, счётчики"""
    # Создаём категории
    smartphones_category = Category("Смартфоны")
    grass_category = Category("Трава")

    # Продукты
    samsung = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "Флагман",
        180000.0,
        5,
        "4.5",
        "S23 Ultra",
        512,
        "Черный"
    )
    grass1 = LawnGrass(
        "Газонная трава",
        "Зеленая",
        500.0,
        10,
        "Россия",
        7,
        "Зеленый"
    )
    grass2 = LawnGrass(
        "Газонная трава 2",
        "Выносливая",
        450.0,
        15,
        "США",
        5,
        "Темно-зеленый"
    )

    # Добавляем
    smartphones_category.add_product(samsung)
    grass_category.add_product(grass1)
    grass_category.add_product(grass2)

    # Проверяем счётчики (как в блоке «Статистика системы» твоего main.py)
    assert Category.total_categories >= 2
    assert Category.total_products >= 3

    # Проверяем формат вывода (как в print(category.products))
    grass_output = grass_category.products
    assert isinstance(grass_output, str)
    assert "Газонная трава, 500.0 руб. Остаток: 10 шт." in grass_output
    assert "Газонная трава 2, 450.0 руб. Остаток: 15 шт." in grass_output
    assert grass_output.count("\n") == 1  # между двумя травами один перенос
