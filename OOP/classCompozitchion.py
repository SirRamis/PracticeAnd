class Engine:
    def start(self):
        print("Двигатель запущен")


class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()
        print("Машина поехала")


engine = Engine()
car = Car(engine)
car.start()