import unittest
from servises.angry_cows import *


class TestMaxMinDistance(unittest.TestCase):
    def test_example_1(self):
        N = 5
        C = 3
        free_sections = [1, 2, 8, 4, 9]
        self.assertEqual(find_max_min_length_between_sections(N, C, free_sections), 3)

    def test_example_2(self):
        N = 6
        C = 4
        free_sections = [7, 2, 14, 5, 10, 12]
        self.assertEqual(find_max_min_length_between_sections(N, C, free_sections), 3)

    def test_example_4(self):
        N = 7
        C = 3
        free_sections = [1, 5, 10, 15, 20, 25, 30]
        self.assertEqual(find_max_min_length_between_sections(N, C, free_sections), 14)

    def test_example_5(self):
        N = 4
        C = 2
        free_sections = [1, 2, 3, 4]
        self.assertEqual(find_max_min_length_between_sections(N, C, free_sections), 3)


if __name__ == '__main__':
    unittest.main()