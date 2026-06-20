class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        # Формат должен совпадать с тем, что ждёт тест: без description, с нужным текстом
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price}, quantity={self.quantity})"

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError(f"Нельзя складывать {type(self).__name__} и {type(other).__name__}")

        # Для базового класса мы просто суммируем цену и количество
        # Но наследники переопределят это, чтобы передать свои параметры
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

    def __str__(self) -> str:
        # Разбиваем строку, чтобы не превысить лимит E501
        return (
            f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт., "
            f"эффективность: {self.efficiency}, модель: {self.model}, "
            f"память: {self.memory} ГБ, цвет: {self.color}"
        )

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError(f"Нельзя складывать {type(self).__name__} и {type(other).__name__}")

        return type(self)(
            self.name,
            self.description,
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
        # Так как базовый __str__ теперь без description, собираем базовую часть явно
        base_str = f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."
        return f"{base_str}, страна: {self.country}, период прорастания: {self.germination_period}, цвет: {self.color}"

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError(f"Нельзя складывать {type(self).__name__} и {type(other).__name__}")

        return type(self)(
            self.name,
            self.description,
            self.price + other.price,
            self.quantity + other.quantity,
            self.country,
            self.germination_period,
            self.color
        )
