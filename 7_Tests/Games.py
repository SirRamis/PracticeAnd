import random
from playsound import playsound
import pygame
class Person():
    my_list = ["ножницы", "бумага", "камень"]

    def __init__(self, name):
        self.name = name

    def go(self):
        return random.choice(self.my_list)


p1 = Person("Amina1")
p2 = Person("Ramis2")
ch1 = p1.go()
ch2 = p2.go()


def game(ch1, ch2):

    if ch1 == ch2:
        print('Ничья')
        playsound("C:/Users/Ramis/PycharmProjects/PracticeITM/7_Tests/3e3fc081726eb67.mp3")
    elif (ch1 == "камень" and ch2 == "ножницы") or \
            (ch1 == "ножницы" and ch2 == "бумага") or \
            (ch1 == "бумага" and ch2 == "камень"):
        print(f'{p1.name} выйграл')
        playsound('C:/Users/Ramis/PycharmProjects/PracticeITM/7_Tests/d17370ef5b82417.mp3')
        #person1.count += 1
        #print(p1.count)
    else:
        print(f'{p2.name} выйграл')
        playsound('C:/Users/Ramis/PycharmProjects/PracticeITM/7_Tests/zlobnyj-muzhskoj-smeh.mp3')
        #person2.count += 1
        #print(p2.count)

print(f'{p1.name}, вышел {ch1}')
print(f'{p2.name}, вышел {ch2}')
game(ch1, ch2)