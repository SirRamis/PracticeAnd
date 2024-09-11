def my_numbers():
    a = 1
    while True:
        yield a
        a += 1


mygen = my_numbers()

print(next(mygen))
print(next(mygen))
print(next(mygen))
print(next(mygen))

c = (i for i in range(1000000000))
for i in c:
    print(i)