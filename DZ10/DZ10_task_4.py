# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest
import time

@pytest.mark.fixtures("time")
class TestClass:
    def test_1(self, time_start):
        assert 1 + 1 == 2
        time.sleep(1)

    def test_2(self, time_stop):
        assert 1 + 1 == 2
        time.sleep(2)

    def test_3(self):
        assert 1 + 1 == 2
        time.sleep(3)