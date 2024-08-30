class MeansOfTransport:
    def __init__(self, brand, color):
        self.__dict__['brand'] = brand
        self.__dict__['color'] = color

    @property
    def brand(self):
        return self.__dict__['brand']

    @brand.setter
    def brand(self, brand):
        self.__dict__['brand'] = brand

    @property
    def color(self):
        return self.__dict__['color']

    @color.setter
    def color(self, color):
        self.__dict__['color'] = color

# Использование
car = MeansOfTransport("Toyota", "Красная")
car.color = "Белая"
print(car.color)
print(car.brand)
