class MeansOfTransport:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    @property
    def brand(self):
        return self._brand
    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

car = MeansOfTransport("Toyota", "Красная")
car.color="Белая"
print(car.color)
print(car.brand)