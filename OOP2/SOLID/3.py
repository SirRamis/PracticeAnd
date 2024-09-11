from abc import ABC, abstractmethod
class Bird(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def fly(self):
        pass
class SwBird(Bird, ABC):
    @abstractmethod
    def swim(self):
        pass
class Duck(SwBird):
    def fly(self):
        print('Can fly')
    def swim(self):
        print('Can swim')
def process(bird: Bird):
    bird.fly()
duck = Duck('Donald')
process(duck)