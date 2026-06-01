from typing import Optional, Any


class Product:
    """Класс, представляющий товар в интернет-магазине."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __repr__(self) -> str:
        return f"Product(name={self.name}, price={self.__price}, quantity={self.quantity})"

    @property
    def price(self) -> float:
        """Геттер для цены."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для цены с проверкой."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if new_price < self.__price:
            confirmation = input(f"Понизить цену с {self.__price} до {new_price}? (y/n): ")
            if confirmation.lower() != "y":
                return
        self.__price = new_price

    @classmethod
    def new_product(
        cls, product_data: dict[str, Any], existing_products: Optional[list["Product"]] = None
    ) -> "Product":
        """Класс-метод для создания продукта из словаря с проверкой дубликатов."""
        name: str = str(product_data.get("name", ""))
        description: str = str(product_data.get("description", ""))
        price: float = float(product_data.get("price", 0.0))
        quantity: int = int(product_data.get("quantity", 0))

        if existing_products:
            for product in existing_products:
                if product.name == name:
                    product.quantity += quantity
                    product.price = max(product.price, price)
                    return product

        return cls(name, description, price, quantity)
