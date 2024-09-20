import random


class Person():
    my_list = ["ножницы", "бумага", "камень"]

    def __init__(self, name):
        self.name = name

    def go(self):
        return random.choice(self.my_list)


p1 = Person("Farit")
p2 = Person("Ken")
ch1 = p1.go()
ch2 = p2.go()
print(ch1)
print(ch2)
