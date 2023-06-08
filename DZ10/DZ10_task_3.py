# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

@pytest.mark.parametrize('x, y, result', [
    pytest.param(47, 10, 4.7, marks=pytest.mark.smoke),
    pytest.param(-66, -2, -3, marks=pytest.mark.skip("Skip'аем")),
    (-66, -2, 33)],
                         ids=['positive', 'invalid_variable', 'negative'])
def test(x, y, result):
    assert all_division(x, y) == result