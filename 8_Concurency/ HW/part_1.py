def get_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

# Пример использования функции для нахождения делителей числа от 100 до 1000
for number in range(100, 1001):
    divisors = get_divisors(number)
    print(f"Делители числа {number}: {divisors}")
