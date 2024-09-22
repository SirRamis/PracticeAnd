class Integer:
    def __set_name__(self, owner, name):
        self.name = "__" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        print(f"__set__: {self.name} = {value}")
        setattr(instance, self.name, value)

class MeansOfTransport:
    brand = Integer()
    color = Integer()
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color


car = MeansOfTransport("Toyota", "Красная")
print(car.__dict__)
print(car.color)