# Разработай программное обеспечение для сети магазинов. Каждый магазин в этой сети имеет свои особенности, но также существуют общие характеристики, такие как адрес, название и ассортимент товаров. Ваша задача — создать класс Store, который можно будет использовать для создания различных магазинов.

# Класс Store - Магазин
# Конструктор класса Store
class Store:
    def __init__(self, name, adress):
        self.name = name
        self.adress = adress
        self.items = {}
        
    # Метод для добавления товара в ассортимент магазина
    def add_item(self, item_name, price):
        # Добавляет товар с указанной ценой в словарь items
        self.items[item_name] = price
        print(f"Товар '{item_name}' добавлен в магазин '{self.name}' по цене {price}.")
        
    # Метод для удаления товара из ассортимента магазина
    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удален из магазина '{self.name}'.")
        else:
            print(f"Товар '{item_name}' не найден в магазине '{self.name}'.")
            
    # Метод для отображения цены товара по его названию
    def get_price(self, item_name):
        if item_name in self.items:
            return self.items[item_name]
        else:
            return None
        
    # Обновить цену товара
    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара '{item_name}' в магазине {self.name} обновлена до {new_price}.")
        else:
            print(f"Товар '{item_name}' не найден в магазине '{self.name}'.")
            
# Основная программа
store1 = Store("Нямка", "ул. Ленина, 1")
store2 = Store("Близкий", "ул. Пушкина, 10")
store3 = Store("Малоцен", "ул. Гагарина, 5")

# Тестирование методов класса Store
# Добавление товаров
store1.add_item("Хлеб", 50)
store1.add_item("Молоко", 80)
store1.add_item("Яблоки", 120)

store2.add_item("Хлеб", 55)
store2.add_item("Молоко", 85)
store2.add_item("Бананы", 125)

store3.add_item("Хлеб", 30)
store3.add_item("Молоко", 60)
store3.add_item("Апельсины", 150)

# Вывод ассортимента
print("\nИтоговые ассортименты:")
print("Нямка:", store1.items)
print("Близкий:", store2.items)
print("Малоцен:", store3.items)

# Проверка цен
print("\nПроверка цен:")
print("Цена яблок в магазине Нямка:", store1.get_price("Хлеб"))
print("Цена молока в магазине Малоцен:", store3.get_price("Молоко"))
print("Цена арбуза в магазине Близкий:", store2.get_price("Арбуз"))  # None

# Обновление цен
print("\nОбновление цен:")
store1.update_price("Яблоки", 110)
store3.update_price("Апельсины", 120)

# Удаление товара
print("\nУдаление товара:")
store2.remove_item("Бананы")
store1.remove_item("Хлеб")

# Вывод ассортимента
print("\nИтоговые ассортименты:")
print("Нямка:", store1.items)
print("Близкий:", store2.items)
print("Малоцен:", store3.items)