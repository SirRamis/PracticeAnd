import pytest

##Проверка равенства:
def test_addition():
    assert 2 + 3 == 5
##Проверка истинности (True/False):
def test_is_positive():
    assert 5 > 0
##Проверка вхождения (contains):
def test_in_list():
    assert 1 in [1, 2, 3]
##Проверка исключений:

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        1 / 0
##Проверка на близость чисел (для чисел с плавающей точкой):
def test_floats():
    assert abs(0.1 + 0.2 - 0.3) < 1e-9


