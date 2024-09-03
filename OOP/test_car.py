class Car:
    d = 4
    e = 5
    def __init__(self, a=1, b=2, c=3):
        self.a = a
        self.b = b
        self.c = c
    def __del__(self):
        print('del')


c = Car()
print(c.a)
del c
# print(c.d)
# print(c.a)