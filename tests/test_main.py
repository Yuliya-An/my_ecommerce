from src.product import Product
from src.category import Category
from src.utils import load_data


def test_product_creation():
    """Проверка создания товара и его атрибутов."""
    p = Product("Тест", "Описание", 100.0, 10)
    assert p.name == "Тест"
    assert p.price == 100.0
    assert p.quantity == 10


def test_product_str():
    """Проверка строкового отображения продукта (__str__)."""
    p = Product("Ноутбук", "Мощный", 150000.0, 5)
    # Предполагаем формат: "Название, Цена руб. Остаток: Кол-во"
    # Отредактируй строку ниже, если в твоем __str__ другой формат!
    expected = f"{p.name}, {p.price} руб. Остаток: {p.quantity}"
    assert str(p) == expected


def test_product_add():
    """Проверка сложения стоимости продуктов (__add__)."""
    p1 = Product("Мышь", "Беспроводная", 2000.0, 3)   # Итого: 6000
    p2 = Product("Клавиатура", "Механическая", 5000.0, 2)  # Итого: 10000
    total = p1 + p2
    assert total == 16000.0


def test_category_creation():
    """Проверка создания категории."""
    c = Category("Электроника", "Описание категории")
    assert c.name == "Электроника"
    # Исправлено: проверяем, что продукты — это список (даже пустой)
    assert isinstance(c.products, list) or c.products == []


def test_add_product_to_category():
    """Проверка добавления товара в категорию."""
    p = Product("Мышка", "Описание", 500.0, 1)
    c = Category("Периферия", "Описание")
    c.add_product(p)
    # Проверяем наличие объекта товара в списке категории
    assert p in c.products


def test_category_count():
    """Проверка счетчика категорий."""
    Category.category_count = 0
    Category("Кат 1", "Описание")
    Category("Кат 2", "Описание")
    assert Category.category_count == 2


def test_load_data_empty():
    """Проверка загрузки данных из несуществующего файла."""
    result = load_data("non_existent_file.json")
    assert result == []
