class Animal:
    def sound(self):
        raise NotImplementedError("Subclasses must implement this method")

class Cat(Animal):
    def sound(self):
        print("Meow")

class Dog(Animal):
    def sound(self):
        print("Woof")

def s1(a: Animal):
    a.sound()

cat = Cat()
dog = Dog()

s1(cat)  # Выведет: Meow
s1(dog)  # Выведет: Woof
