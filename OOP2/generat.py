def my_generator():
    yield 1
    yield 2
    yield 3

# Использование
gen = my_generator()
for value in gen:
    print(value)
