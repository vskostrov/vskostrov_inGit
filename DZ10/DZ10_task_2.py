# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

# Несколько цифр (smoke)
@pytest.mark.smoke
def test_positive():
    assert all_division(47, 10) == 4.7

# Одно число
def test_one_number():
    assert all_division(26, ) == 26

# Отрицательные числа
def test_negative_numbers():
    assert all_division(-66, -2) == 33

# Деление на строку
def test_invalid_variable():
    try:
        all_division(15, '67')
    except TypeError:
        assert True

# Тест деления на нуль (smoke)
@pytest.mark.smoke
def test_zero():
    try:
        all_division(15, 0, 3)
    except ZeroDivisionError:
        assert True