import json
from typing import List
from src.category import Category
from src.product import Product


def load_data(filename: str) -> List[Category]:
    """Загружает данные о категориях и продуктах из JSON-файла с защитой от ошибок."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # Если файла нет или он битый, возвращаем пустой список, чтобы программа не упала
        return []

    categories = []
    for category_data in data:
        # Создаем список продуктов для данной категории
        products = [
            Product(
                name=prod["name"],
                description=prod["description"],
                price=prod["price"],
                quantity=prod["quantity"]
            )
            for prod in category_data.get("products", [])
        ]
        # Создаем саму категорию и передаем ей список продуктов
        category = Category(
            name=category_data["name"],
            description=category_data["description"],
            products=products
        )
        categories.append(category)
    return categories
