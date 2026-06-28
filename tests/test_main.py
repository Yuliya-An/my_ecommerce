import pytest
from src.product import Product, Smartphone, LawnGrass
from src.category import Category


def test_smartphone_creation():
    s = Smartphone(
        "Samsung", "Desc", 1000.0, 10, "High", "S23", "256GB",
        "Sерый"
    )
    assert s.name == "Samsung"
    assert s.price == 1000.0
    assert s.color == "Sерый"


def test_lawn_grass_creation():
    g = LawnGrass(
        "Трава", "Desc", 500.0, 20, "Россия", "7 дней",
        "Зеленый"
    )
    assert g.name == "Трава"
    assert g.price == 500.0
    assert g.color == "Зеленый"


def test_product_str():
    p = Product("Товар", "Описание", 100.0, 5)
    assert str(p) == "Товар, 100.0 руб. Остаток: 5 шт."


def test_category_creation():
    cat = Category("Электроника", "Описание категории")
    assert cat.name == "Электроника"
    assert cat.description == "Описание категории"


def test_add_valid_product():
    cat = Category("Электроника", "Desc")
    p = Product("Товар", "Desc", 100.0, 5)
    cat.add_product(p)
    assert cat.product_count == 1


def test_add_invalid_product_raises_type_error():
    cat = Category("Электроника", "Desc")
    with pytest.raises(TypeError):
        cat.add_product("Не продукт")


def test_products_property_returns_correct_string_format():
    p1 = Product("Товар 1", "Описание 1", 100.0, 5)
    p2 = Product("Товар 2", "Описание 2", 200.0, 3)
    category = Category("Мои товары", "Описание товаров")
    category.add_product(p1)
    category.add_product(p2)
    expected = "Товар 1, 100.0 руб. Остаток: 5 шт.\nТовар 2, 200.0 руб. Остаток: 3 шт."
    assert category.products == expected

    def test_category_iteration():
        p1 = Product("P1", "Desc1", 100.0, 2)
        p2 = Product("P2", "Desc2", 200.0, 3)
        category = Category("Итерация тест", "Описание для теста")
        category.add_product(p1)
        category.add_product(p2)

        products = list(category)
        assert len(products) == 2
        assert products[0] == p1
        assert products[1] == p2

    def test_main_scenario_full_flow():
        cat = Category("Смартфоны", "Описание смартфонов")
        s1 = Smartphone(
            "S1", "D1", 50000.0, 10, "High", "Model1", "128GB",
            "Черный"
        )
        s2 = Smartphone(
            "S2", "D2", 60000.0, 5, "Ultra", "Model2", "256GB",
            "Белый"
        )

        cat.add_product(s1)
        cat.add_product(s2)

        assert cat.product_count == 2
        assert "S1, 50000.0 руб. Остаток: 10 шт." in cat.products
        assert "S2, 60000.0 руб. Остаток: 5 шт." in cat.products

    def test_product_addition_logic():
        p1 = Product("Товар 1", "D1", 100.0, 5)
        p2 = Product("Товар 2", "D2", 200.0, 3)
        result = p1 + p2
        assert isinstance(result, (float, int))
        assert result == 1100.0

    def test_invalid_product_addition_raises_type_error():
        s = Smartphone(
            "S", "D", 100.0, 1, "High", "M1", "1GB", "Sерый"
        )
        g = LawnGrass(
            "G", "D", 10.0, 1, "RU", "1d", "Зеленый"
        )
        with pytest.raises(TypeError):
            _ = s + g
