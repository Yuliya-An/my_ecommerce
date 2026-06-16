class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError('Нельзя складывать товары разных классов!')
        return type(self)(
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
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Нельзя складывать товары разных классов")
        return Smartphone(
            f"{self.name}+{other.name}",
            f"{self.description}+{other.description}",
            self.price + other.price,
            self.quantity + other.quantity,
            self.efficiency,
            self.model,
            self.memory,
            self.color
        )


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Нельзя складывать газонную траву с другими товарами")
        return LawnGrass(
            f"{self.name}+{other.name}",
            f"{self.description}+{other.description}",
            self.price + other.price,
            self.quantity + other.quantity,
            self.country,
            self.germination_period,
            self.color
        )
