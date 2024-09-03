class MeansOfTransport:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def show_color(self):
        return self.color

    def show_brand(self):
        return self.brand

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_brand(self):
        return self.brand

    def set_brand(self, brand):
        self.brand = brand


class Moped(MeansOfTransport):
    def __init__(self, kols=2):
        self.kols = kols

    @staticmethod
    def timer(a, b):
        return a / b


class Car(MeansOfTransport):
    car_drive = 4
    def __init__(self, kols=4, doors=3, strong=2.5):
        self.kols = kols
        self._doors = doors
        self.__strong = strong
    @classmethod
    def show_dr(cls):
        return cls.car_drive

m = Moped.timer(300, 90)
print(m)
