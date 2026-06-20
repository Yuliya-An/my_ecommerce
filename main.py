from src.product import Smartphone, LawnGrass
from src.category import Category

# Создаем категории
smartphones_category = Category("Смартфоны")
grass_category = Category("Трава")

# Создаем продукты
samsung = Smartphone(
    "Samsung Galaxy S23 Ultra", "Флагманский смартфон",
    180000.0, 5, 4.5, "S23 Ultra", 512, "Черный"
)
iphone = Smartphone(
    "iPhone 15", "Новейший айфон",
    210000.0, 8, 4.8, "15 Pro", 256, "Титан"
)
xiaomi = Smartphone(
    "Xiaomi Redmi Note 11", "Бюджетный смартфон",
    31000.0, 14, 4.2, "Note 11", 128, "Синий"
)

grass1 = LawnGrass(
    "Газонная трава", "Зеленая трава",
    500.0, 10, "Россия", 7, "Зеленый"
)
grass2 = LawnGrass(
    "Газонная трава 2", "Выносливая трава",
    450.0, 15, "США", 5, "Темно-зеленый"
)

# Наполняем категорию смартфонами
smartphones_category.add_product(samsung)
smartphones_category.add_product(iphone)
smartphones_category.add_product(xiaomi)

# Наполняем категорию травой (теперь две травы, как нужно)
grass_category.add_product(grass1)
grass_category.add_product(grass2)

# Демонстрация защиты от неправильных типов (обязательно для задания!)
print("--- Проверка защиты типа ---")
try:
    smartphones_category.add_product("Это не смартфон, а просто строка")  # type: ignore[arg-type]
except TypeError as e:
    print(f"Поймали ошибку: {e}")

print("---------------------------\n")

# Демонстрация сложения объектов
print("--- Проверка сложения ---")
total_smartphones = samsung + iphone
print(f"Результат сложения смартфонов: {total_smartphones}")

total_grass = grass1 + grass2  # Складываем две разные травы
print(f"Результат сложения травы: {total_grass}")

# Попытка сложить разные типы (должна вызвать ошибку)
print("Пробуем сложить смартфон и траву...")
try:
    error_sum = samsung + grass1
except TypeError as e:
    print(f"Поймали ожидаемую ошибку при сложении разных типов: {e}")

print("---------------------------\n")

# Вывод всех продуктов в категориях
# Важно: здесь используется свойство products, которое возвращает одну строку с переносами
print("--- Содержимое категорий ---")
print("Смартфоны:")
print(smartphones_category.products)
print("\nТрава:")
print(grass_category.products)
print("----------------------------\n")

# Проверка работы классовых счётчиков (обязательно для задания!)
print("--- Статистика системы ---")
print(f"Всего категорий: {Category.total_categories}")
print(f"Всего товаров: {Category.total_products}")
