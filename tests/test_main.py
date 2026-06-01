from src.product import Product
from src.category import Category
from src.utils import load_data


def test_product_creation():
    """Проверка создания товара и его атрибутов."""
    p = Product("Тест", "Описание", 100.0, 10)
    assert p.name == "Тест"
    assert p.price == 100.0
    assert p.quantity == 10


def test_category_creation():
    """Проверка создания категории."""
    c = Category("Электроника", "Описание категории")
    assert c.name == "Электроника"
    assert c.products == ""


def test_add_product_to_category():
    """Проверка добавления товара в категорию."""
    p = Product("Мышка", "Описание", 500.0, 1)
    c = Category("Периферия", "Описание")
    c.add_product(p)
    assert "Мышка" in c.products


def test_category_count():
    """Проверка счетчика категорий."""
    Category.category_count = 0
    Category("Кат 1", "Описание")
    Category("Кат 2", "Описание")
    assert Category.category_count == 2


def test_product_count_in_category():
    """Проверка счетчика товаров ВНУТРИ категории."""
    c = Category("Тест", "Описание")
    p1 = Product("Т1", "Оп", 10.0, 1)
    p2 = Product("Т2", "Оп", 20.0, 2)
    c.add_product(p1)
    c.add_product(p2)
    assert len(c._Category__products) == 2


def test_load_data_empty():
    """Проверка загрузки данных из несуществующего файла (покрытие utils)."""
    result = load_data("non_existent_file.json")
    assert result == []
