import pytest
from main import calculate_average

@pytest.fixture(scope='session', autouse=True)
def setup_tests():
    global TESTER_NAME
    TESTER_NAME = 'Uydnikov Vladimir'
    print(f'\nTests executed by {TESTER_NAME}\n')

@pytest.mark.parametrize('input_data, expected', [
    ([1.7, 2.8, 3.9], 2),
    ([-1.7, -2.8, -3.9], -3),
    ([1.7, -2.8, 3.9], 0),
    ([], None)
])
def test_calculate_average(input_data, expected):
    assert calculate_average(input_data) == expected
