
from Concurency_8.HW_8.part_1.part_1 import get_divisors
def test_get_divisors():
    # Тест 1: Проверка делителей числа 10
    assert get_divisors(10) == [1, 2, 5, 10], "Тест 1 не пройден"

    # Тест 2: Проверка делителей числа 25
    assert get_divisors(25) == [1, 5, 25], "Тест 2 не пройден"

    # Тест 3: Проверка делителей числа 7 (простое число)
    assert get_divisors(7) == [1, 7], "Тест 3 не пройден"

    # Тест 4: Проверка делителей числа 100
    assert get_divisors(100) == [1, 2, 4, 5, 10, 20, 25, 50, 100], "Тест 4 не пройден"

    # Тест 5: Проверка делителей числа 1 (особый случай)
    assert get_divisors(1) == [1], "Тест 5 не пройден"

    print("Все тесты пройдены!")


# Вызов функции для тестирования
test_get_divisors()



def test_get_divisors_positive():
    # Тест 1: Проверка делителей числа 12
    result = get_divisors(12)
    expected = [1, 2, 3, 4, 6, 12]
    assert result == expected, f"Ожидаемый результат {expected}, но получен {result}"

    # Тест 2: Проверка делителей числа 15
    result = get_divisors(15)
    expected = [1, 3, 5, 15]
    assert result == expected, f"Ожидаемый результат {expected}, но получен {result}"

    # Тест 3: Проверка делителей числа 28 (совершенное число)
    result = get_divisors(28)
    expected = [1, 2, 4, 7, 14, 28]
    assert result == expected, f"Ожидаемый результат {expected}, но получен {result}"

    print("Все положительные тесты пройдены успешно!")


# Запуск теста
test_get_divisors_positive()

