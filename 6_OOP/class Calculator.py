class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def summ(self):
        return self.a + self.b

c = Calculator(3,5)
print(c.summ())

class Calc2(Calculator):
    def str_calc(self, a, b):
        return str(a) + str(b)

str_c = Calc2("My"," name")
print(str_c.summ())