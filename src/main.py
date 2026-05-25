import json
from typing import List


class Product:
    """Класс, представляющий товар в интернет-магазине."""

    product_count = 0

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        Product.product_count += 1

    def __repr__(self) -> str:
        return f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"


class Category:
    """Класс, представляющий категорию товаров."""

    category_count = 0

    def __init__(self, name: str, description: str, products: List[Product] | None = None):
        self.name = name
        self.description = description
        self.products = products if products is not None else []
        Category.category_count += 1

    def add_product(self, product: Product) -> None:
        """Добавляет товар в категорию."""
        self.products.append(product)

    def __repr__(self) -> str:
        return f"Category(name={self.name}, products_count={len(self.products)})"


if __name__ == "__main__":
    # Создание товаров
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    # Создание первой категории со списком товаров
    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, "
                         "но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(Category.category_count)
    print(Product.product_count)

    # Создание четвертого товара и второй категории
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, "
                         "станет вашим другом и помощником",
                         [product4])

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    # Финальная проверка счетчиков
    print(Category.category_count)
    print(Product.product_count)


def load_data(filename: str) -> List[Category]:
    with open(filename, encoding='utf-8') as f:
        data = json.load(f)

    categories = []
    for category_data in data:
        products = []
        for prod_data in category_data["products"]:
            product = Product(
                name=prod_data["name"],
                description=prod_data["description"],
                price=prod_data["price"],
                quantity=prod_data["quantity"]
            )
            products.append(product)

        category = Category(
            name=category_data["name"],
            description=category_data["description"],
            products=products
        )
        categories.append(category)

    return categories

if __name__ == "__main__":
    categories = load_data("products.json")
    print(f"Загружено {len(categories)} категорий.")
    total_products = sum(len(cat.products) for cat in categories)
    print(f"Загружено {total_products} продуктов.")
