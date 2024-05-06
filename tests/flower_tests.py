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

    def test_unique_vertices(self):
        graph = Graph(self.test_csv_file)
        num_vertices = graph.unique_vertices(self.test_csv_file)
        self.assertEqual(num_vertices, 6)

    def test_add_edge(self):
        graph = Graph(self.test_csv_file)
        graph.add_edge("A", "B", 3)
        graph.add_edge("B", "C", 4)
        self.assertEqual(graph.edges_matrix[0][1], 3)
        self.assertEqual(graph.edges_matrix[1][2], 4)

    def test_dfs(self):
        graph = Graph(self.test_csv_file)
        graph.add_edge("A", "B", 3)
        graph.add_edge("B", "C", 4)
        path = graph.dfs(0, 2)
        self.assertEqual(path, [0, 1, 2])

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
