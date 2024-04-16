import unittest
from src.gas_for_penguins import inaccessible_cities


class TestGasForPenguins(unittest.TestCase):
    def test_case_1(self):
        my_cities = {'A', 'B', 'C', 'D', 'E'}
        my_gas_stations = ['g1', 'g2']
        my_gas_lines = [('g1', 'A'), ('g1', 'B'), ('A', 'D'), ('B', 'D'), ('g2', 'C'), ('C', 'B')]

        self.assertEqual(inaccessible_cities(my_cities, my_gas_stations, my_gas_lines),
                         {'g1': ['C', 'E'], 'g2': ['E', 'A']})

    def test_case_2(self):
        my_cities = {'A', 'B'}
        my_gas_stations = ['g1']
        my_gas_lines = [('g1', 'A'), ('A', 'B')]

        self.assertEqual(inaccessible_cities(my_cities, my_gas_stations, my_gas_lines),
                         {'g1': []})
