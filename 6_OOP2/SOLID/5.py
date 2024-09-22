#Принцип инверсии зависимостей

from abc import ABC, abstractmethod


class Switch(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    def turn_off(self):
        pass
class Liting(Switch):
    def turn_on(self):
        print('Vkluchena lampa')
    def turn_off(self):
        print('vikluchena lampa')

class Conditioner(Switch):
    def turn_on(self):
        print('Vkluchen conditioner')
    def turn_off(self):
        print('vikluchen conditioner')

conditioner = Conditioner()
conditioner.turn_off()