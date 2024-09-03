import logging

logging.basicConfig(level=logging.DEBUG, filename='my_logging.log', format='%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d) [%(filename)s]', datefmt='%d/%m/%Y %I:%M:%S',
                     encoding = 'utf-8', filemode='a+')

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
        logging.info('sozdan')

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
tr.set_brand('rtrtr')

class Car(Transport):
    car_drive = 4
    def __init__(self, c_wheels=4, engine=2.5, doors=3):
        self.c_wheels = c_wheels
        self._engine = engine
        self.__doors = doors

    def write_of_display(self):
        return f"количество колес : {self.c_wheels} штук"
    @classmethod
    def w_of_displ(cls):
        return Car.car_drive

    def __str__(self):
        return f"Этот {self.c_wheels} , {self.__doors} дверя, и {self._engine} ."


    def __repr__(self):
        return f"Этот метод репр метод"


tc = Car()
print(Car.__dict__)
print(tc._engine)
print(tc._Car__dors)
tc.c_wheels = 5
print(tc.write_of_display())
print(tc.set_color('gfg'))
print(tc.get_color())


class Moped(Transport):
    def __init__(self, c_wheels=2):
        self.c_wheels = c_wheels

    @staticmethod
    def s_time(x, y):
        return f"Это то время за которое проедет мопед {x / y}"

tc = Moped()
print(tc.c_wheels)
print(tc.s_time(600,80))