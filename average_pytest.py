import pytest
from average import calculate_average


@pytest.fixture(scope='session', autouse=True)
def setup_tests():
    global TESTER_NAME
    TESTER_NAME = 'Uydnikov Vladimir'
    print(f'\nTests executed by {TESTER_NAME}\n')


@pytest.mark.parametrize('input_data, expected',
                         [
                            ([1.7, 2.8, 3.9], 2),  # Положительные числа
                            ([-1.7, -2.8, -3.9], -3),  # Отрицательные числа
                            ([1.7, -2.8, 3.9], 0),  # Смешанный случай
                            ([], None),  # Пустой список
                          ]
                        )
def test_calculate_average(input_data, expected):
    actual_result = calculate_average(input_data)
    assert actual_result == expected, f"Ошибка при проверке набора {input_data}"
