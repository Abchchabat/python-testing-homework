import unittest
from main import calculate_average

class TestCalculateAverage(unittest.TestCase):
    def setUp(self):
        self.tester_name = 'Uydnikov Vladimir'
        print(f'Tested by {self.tester_name}')

    def test_positive_numbers(self):
        result = calculate_average([1.7, 2.8, 3.9])
        self.assertEqual(result, 2)

    def test_negative_numbers(self):
        result = calculate_average([-1.7, -2.8, -3.9])
        self.assertEqual(result, -3)

    def test_mixed_numbers(self):
        result = calculate_average([1.7, -2.8, 3.9])
        self.assertEqual(result, 0)

    def test_empty_list(self):
        result = calculate_average([])
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
