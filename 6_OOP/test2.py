class Transport:
    brand = "Tayota"
    color = "Red"

    def show_color(self):
        return f"цвет транспортного средства: {self.color}"

    def show_brand(self):
        return f"марка транспортного средства: {self.brand}"

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def get_brand(self):
        return f"марка транспортного средства: {self.brand}"

    def set_brand(self, brand):
        self.brand = brand

    def get_color(self):
        return f"цвет транспортного средства: {self.color}"

    def set_color(self, color):
        self.color = color


tr = Transport("Toyota", "Blue")
print(tr.__dict__)
print(tr.show_color())
print(tr.show_brand())
print(tr.get_color())
print(Transport.color)


class Car:
    def __init__(self, c_wheels=4):
        self.c_wheels = c_wheels

tc = Car()
print(tc.c_wheels)

class Moped:
    def __init__(self, c_wheels=2):
        self.c_wheels = c_wheels

tc = Moped()
print(tc.c_wheels)