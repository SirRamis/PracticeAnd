from playsound import playsound
from abc import ABC, abstractmethod
class Animals(ABC):
    @abstractmethod
    def sound(self):
        pass

class Cat(Animals):
    def sound(self):
        return playsound('3e3fc081726eb67.mp3')

class Dog(Animals):
    def sound(self):
        return playsound('dog-bark-15.mp3')

do = Dog()
do.sound()
ca = Cat()
ca.sound()