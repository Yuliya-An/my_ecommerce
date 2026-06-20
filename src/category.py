from src.product import Product


class Category:
    # Классовые атрибуты инициализируются здесь, в самом верху.
    # Это наши глобальные счётчики для всей системы.
    total_categories = 0
    total_products = 0

    def __init__(self, name: str):
        self.name = name
        self.__products: list[Product] = []  # <-- добавили : list[Product]
        # Увеличиваем счётчик категорий при создании каждого нового экземпляра
        Category.total_categories += 1

    def __str__(self) -> str:
        return f"Категория: {self.name}"

    def __repr__(self) -> str:
        return f"Category(name='{self.name}')"

    def add_product(self, product: Product):
        # Проверка типа обязательна для задания
        if not isinstance(product, Product):
            raise TypeError("В категорию можно добавлять только объекты класса Product")

        self.__products.append(product)
        Category.total_products += 1

    @property
    def products(self) -> str:
        """
        Возвращает ОДНУ строку с товарами. Каждый товар с новой строки.
        Формат строго такой: "Название, Цена руб. Остаток: Количество шт."
        Это нужно, чтобы при print() не было квадратных скобок и кавычек.
        """
        if not self.__products:
            return ""
        lines = []
        for p in self.__products:
            lines.append(f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт.")
        return "\n".join(lines)

    @property
    def product_count(self) -> int:
        return len(self.__products)

    def __iter__(self):
        # Позволяет делать: for product in category:
        return iter(self.__products)
