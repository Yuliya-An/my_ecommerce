class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price}, quantity={self.quantity})"

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError(f"Нельзя складывать {type(self).__name__} и {type(other).__name__}")
        return Product(
            self.name,
            self.description,
            self.price + other.price,
            self.quantity + other.quantity
        )


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        return (f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт., "
                f"эффективность: {self.efficiency}, модель: {self.model}, "
                f"память: {self.memory} ГБ, цвет: {self.color}")

    def __add__(self, other):
        if not isinstance(other, Smartphone):
            raise TypeError(f"Нельзя складывать {type(self).__name__} и {type(other).__name__}")
        return super().__add__(other)


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        return (f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт., "
                f"страна: {self.country}, период прорастания: {self.germination_period}, "
                f"цвет: {self.color}")

    def __add__(self, other):
        if not isinstance(other, LawnGrass):
            raise TypeError(f"Нельзя складывать {type(self).__name__} и {type(other).__name__}")
        return super().__add__(other)
