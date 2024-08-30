class MeansOfTransport:
    def __init__(self, brand, color):
        self.__brand = brand
        self.__color = color
    @property
    def brand(self):
        return self.__brand
    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

car = MeansOfTransport("Toyota", "Красная")
car.color="Белая"
print(car.color)
print(car.brand)