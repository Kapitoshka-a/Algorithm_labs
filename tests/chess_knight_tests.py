import unittest
from src.chess_knight import shortest_knight_path


class TestChessKnight(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(shortest_knight_path((7, 0), (0, 7)), 6)

    def test_case_2(self):
        self.assertEqual(shortest_knight_path((0, 0), (1, 2)), 1)

    def test_case(self):
        self.assertEqual(shortest_knight_path((0, 0), (1, 2), 2), None)
