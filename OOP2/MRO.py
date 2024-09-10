class A:
    def method(self):
        print("Method in A")

class B(A):
    def method(self):
        print("Method in B")

class C(A):
    def method(self):
        print("Method in C")

class D(B, C):
    pass

# Создаём экземпляр класса D
obj = D()

# Вызываем метод
obj.method()  # Вывод: Method in B

# Проверяем MRO для класса D
print(D.mro())  # Вывод: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
