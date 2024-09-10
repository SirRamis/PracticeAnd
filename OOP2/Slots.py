class MyClass:
    __slots__ = ['name', 'age']  # Ограничиваем атрибуты только 'name' и 'age'

    def __init__(self, name, age):
        self.name = name
        self.age = age

# Создаём экземпляр класса
obj = MyClass("Alice", 30)

# Доступ к атрибутам
print(obj.name)  # Вывод: Alice
print(obj.age)   # Вывод: 30

# Попытка добавить новый атрибут вызовет ошибку
# obj.address = "123 Street"  # AttributeError: 'MyClass' object has no attribute 'address'
