import cProfile
def get_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors
def main():
    divisors = get_divisors(102)
    print(divisors)

if __name__ == '__main__':  # Пример использования функции для нахождения делителей числа от 100 до 1000
    # for number in range(100, 200):
    #     divisors = get_divisors(number)
    #     print(f"Делители числа {number}: {divisors}")

    cProfile.run('main()')

def test_get_divisors():
    assert get_divisors(102) == [1, 2, 3, 6, 17, 34, 51, 102]