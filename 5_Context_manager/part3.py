class Person:

    def __init__(self, name, age, ear):
        self.name = name
        self.age = age
        self.ear = ear


cat = Person('Fixi', 23, 1987)
print(cat.name)

# class Person2:
#    def __init__(self, name):
#       self.name = name
#
#    def say_hello(self):
#       print("Hello, my name is", self.name)

# person1 = Person("Alice")
# person1.age = 25
# print(person1.__dict__)
