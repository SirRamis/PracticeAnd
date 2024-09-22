#from playsound import playsound
from abc import ABC, abstractmethod
class Animals(ABC):
    @abstractmethod
    def sound(self):
        pass

class Cat(Animals):
    def sound(self):
        #return playsound('3e3fc081726eb67.mp3')
        print(f'MIAU')

class Dog(Animals):
    def sound(self):
        #return playsound('dog-bark-15.mp3')
        print(f'GAF')


# dog = Dog()
# dog.sound()
# cat = Cat()
# cat.sound()

def s1(a:Animals):
    a.sound()

cat = Cat()
dog = Dog()
s1(cat)
s1(dog)