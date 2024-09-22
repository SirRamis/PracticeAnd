# zeroes = [0 for i in range(100)]
# for i in zeroes:
#     print(i)
# print(zeroes)

# n = int(input())
# a = [i for i in range(1, n+1)]
# print(a)

# result = []
# for x in range(15):
#     if x % 2 == 0:
#         result.append(x * x)
# print(result)
#
# resul = [x * x for x in range(15) if x % 2 == 0]
# print(resul)

# a = int(input())
# b = [a for a in range(a)if a % 2 == 0]
# print(b)

a = int(input())
b = [a//i for i in range(1, a+1)if a % i == 0]
print(b)