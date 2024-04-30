import unittest
from src.flower import Graph


class TestGraph(unittest.TestCase):

    def test_add_edge(self):
        graph = Graph(4)
        graph.add_edge("A", "B", 5)
        self.assertEqual(graph.adj_matrix, [[0, 5, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])

    def test_dfs(self):
        graph = Graph(4)
        graph.add_edge("A", "B", 5)
        graph.add_edge("B", "C", 10)
        graph.add_edge("C", "D", 15)
        self.assertEqual(graph.dfs(0, 3), [0, 1, 2, 3])

    def test_ford_fulkerson(self):
        graph = Graph(4)
        graph.add_edge("A", "B", 5)
        graph.add_edge("B", "C", 10)
        graph.add_edge("C", "D", 15)
        max_flow = graph.ford_fulkerson("A", "D")
        self.assertEqual(max_flow, 5)

    def test_build_graph_from_csv(self):
        graph = Graph(10)
        graph.build_graph_from_csv("test_roads.csv")
        expected_adj_matrix = [
             [0, 10, 5, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 8, 0, 0, 12, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 6, 0, 0, 0, 15, 7, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(graph.adj_matrix, expected_adj_matrix)


if __name__ == '__main__':
    unittest.main()
