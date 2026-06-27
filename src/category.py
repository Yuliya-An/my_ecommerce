from src.product import Product


class Category:
    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("В категорию можно добавлять только объекты класса Product")
        self.__products.append(product)

    @property
    def product_count(self):
        return len(self.__products)

    @property
    def products(self):
        res = []
        for p in self.__products:
            res.append(f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт.")
        return "\n".join(res)

    def __iter__(self):
        return iter(self.__products)
