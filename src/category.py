class Category:
    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products if products is not None else []

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.products)
        return f"Категория: {self.name}. Всего товаров: {total_quantity} шт."

    def __iter__(self):
        return iter(self.products)
