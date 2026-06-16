from src.product import Product, Smartphone, LawnGrass
from src.category import Category

if __name__ == '__main__':
    # Создаем базовые продукты
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    # Создаем категорию и добавляем туда продукты
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(str(category1))
    print(category1.products)

    # Проверяем сложение продуктов одного класса
    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)

    # Проверяем сложение разных классов (должна быть ошибка TypeError)
    smartphone = Smartphone("S1", "Desc", 100.0, 5, "High", "M1", "256GB", "Black")
    grass = LawnGrass("G1", "Desc", 10.0, 10, "RU", "7d", "Green")

    try:
        smartphone + grass
        print("ОШИБКА: Сложение разных классов не вызвало TypeError!")
    except TypeError as e:
        print(f"Ожидаемая ошибка: {e}")

    # Проверяем добавление не-продукта в категорию
    try:
        category1.add_product("Я не продукт")
        print("ОШИБКА: Добавление строки не вызвало TypeError!")
    except TypeError as e:
        print(f"Ожидаемая ошибка: {e}")
