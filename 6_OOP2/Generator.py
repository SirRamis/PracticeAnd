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
print('------')

# c = (i for i in range(1000000000))
# for i in c:
#     print(i)
s = [5,6,7,8,9]
def genf():
    for i in s:
        yield i
a = genf()
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))