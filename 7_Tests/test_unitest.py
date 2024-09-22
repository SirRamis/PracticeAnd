##Проверка равенства:

import unittest

class TestMath(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 3, 5)
##Проверка истинности (True/False):


class TestBoolean(unittest.TestCase):
    def test_is_positive(self):
        self.assertTrue(5 > 0)
##Проверка вхождения (contains):


class TestContainment(unittest.TestCase):
    def test_in_list(self):
        self.assertIn(1, [1, 2, 3])
##Проверка исключений:


class TestExceptions(unittest.TestCase):
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            1 / 0
##Проверка на близость чисел (для чисел с плавающей точкой):


class TestFloats(unittest.TestCase):
    def test_floats(self):
        self.assertAlmostEqual(0.1 + 0.2, 0.3, places=9)