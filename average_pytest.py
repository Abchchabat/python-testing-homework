import pytest
from average import calculate_average


@pytest.fixture(scope="module")
def tester():
    return {'tester': 'Ivan Petrov'}


@pytest.mark.parametrize("input_data,expected",
                         [
                             ([1.5, 2.5, 3.5], 2),
                             ([-1.5, -2.5, -3.5], -2),
                             ([1.5, -2.5, 3.5], 1),
                             ([], None)
                         ])
def test_calculate_average(input_data, expected, tester):
    assert calculate_average(input_data) == expected
    print(f'{tester["tester"]}: Проверено среднее значение {input_data}, ожидаемое: {expected}.')
