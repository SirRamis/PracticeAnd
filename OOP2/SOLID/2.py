import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Crug(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * math.pi

class Kvadrat(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2