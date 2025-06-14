import unittest
from average import calculate_average


class TestCalculateAverage(unittest.TestCase):
    def setUp(self):
        self.tester_name = 'Ivan Petrov'
        print(f'Tested by {self.tester_name}')
        
    def test_positive_numbers(self):
        result = calculate_average([1.5, 2.5, 3.5])
        expected_result = 2
        self.assertEqual(result, expected_result)

    def test_negative_numbers(self):
        result = calculate_average([-1.5, -2.5, -3.5])
        expected_result = -2
        self.assertEqual(result, expected_result)

    def test_mixed_numbers(self):
        result = calculate_average([1.5, -2.5, 3.5])
        expected_result = 1
        self.assertEqual(result, expected_result)

    def test_empty_list(self):
        result = calculate_average([])
        expected_result = None
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
