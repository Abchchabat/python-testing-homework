import unittest
from average import calculate_average


class TestCalculateAverage(unittest.TestCase):
    def setUp(self):
        self.tester_name = 'Uydnikov Vladimir'
        print(f'Tested by {self.tester_name}')

    def test_positive_numbers(self):
        """Проверяем положительное число"""
        result = calculate_average([1.7, 2.8, 3.9])
        expected_result = 2
        self.assertEqual(result, expected_result)

    def test_negative_numbers(self):
        """Проверяем отрицательные числа"""
        result = calculate_average([-1.7, -2.8, -3.9])
        expected_result = -3
        self.assertEqual(result, expected_result)

    def test_mixed_numbers(self):
        """Проверяем смешанные положительные и отрицательные числа"""
        result = calculate_average([1.7, -2.8, 3.9])
        expected_result = 0
        self.assertEqual(result, expected_result)

    def test_empty_list(self):
        """Проверяем пустой список"""
        result = calculate_average([])
        expected_result = None
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
