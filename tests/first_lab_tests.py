import unittest
from servises.first_lab import *


class TestLongestPeak(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(find_longest_peak([1, 2, 3, 4, 5, 6]), None)

    def test_case_2(self):
        self.assertEqual(find_longest_peak([6, 5, 4, 3, 2, 1]), None)

    def test_case_3(self):
        self.assertEqual(find_longest_peak([1, 3, 5, -2, 1, 10, 15, 0, -1, -4, 4, 5, 4]),
                         [-2, 1, 10, 15, 0, -1, -4])

    def test_case_4(self):
        self.assertEqual(find_longest_peak([1, 4, 2, 10, 20, 30, 40]), [1, 4, 2])


if __name__ == '__main__':
    unittest.main()
