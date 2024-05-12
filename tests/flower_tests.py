import os
import unittest
from src.flower import Graph


class TestFlowerGraph(unittest.TestCase):
    def setUp(self):
        self.test_csv_file = "test_roads.csv"
        with open(self.test_csv_file, 'w') as file:
            file.write("A,B,3\n")
            file.write("B,C,4\n")
            file.write("C,D,5\n")

    def tearDown(self):
        if os.path.exists(self.test_csv_file):
            os.remove(self.test_csv_file)

    def test_ford_fulkerson(self):
        graph = Graph(self.test_csv_file)
        graph.build_graph_from_csv()
        max_flow = graph.ford_fulkerson("A", "D")
        self.assertEqual(max_flow, 3)

    def test_max_flow(self):
        graph = Graph(self.test_csv_file)
        graph.build_graph_from_csv()
        sources = ["A"]
        sinks = ["D"]
        max_flow = graph.max_flow(sources, sinks)
        self.assertEqual(max_flow, 3)


if __name__ == '__main__':
    unittest.main()
