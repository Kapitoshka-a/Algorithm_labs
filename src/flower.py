import csv
from typing import List, Set

DEFAULT_START_VIRTUAL_VERTEX = "START_VIRTUAL_VERTEX"
DEFAULT_END_VIRTUAL_VERTEX = "END_VIRTUAL_VERTEX"
VIRTUAL_VERTEX_NUM = 2


class Graph:
    def __init__(self, csv_file: str):
        self.list_of_vertices = []
        self.csv_file = csv_file
        unique_vertices = self.unique_vertices(csv_file)
        self.edges_matrix = [[0] * unique_vertices for _ in range(unique_vertices)]

    @staticmethod
    def unique_vertices(csv_file: str) -> int:
        unique_vertices = set()
        with open(csv_file, "r") as file:
            for line in file:
                if line[0] not in unique_vertices:
                    unique_vertices.add(line[0])
                if line[1] not in unique_vertices:
                    unique_vertices.add(line[1])
        return len(unique_vertices) + VIRTUAL_VERTEX_NUM

    def add_edge(self, current_vertex: str, next_vertex: str, weight: float):
        if current_vertex not in self.list_of_vertices:
            self.list_of_vertices.append(current_vertex)
        if next_vertex not in self.list_of_vertices:
            self.list_of_vertices.append(next_vertex)
        self.edges_matrix[self.list_of_vertices.index(current_vertex)][
            self.list_of_vertices.index(next_vertex)] = weight

    def add_virtual_vertexes(self, sources: list, sinks: list):
        for vertex in sources:
            self.add_edge(DEFAULT_START_VIRTUAL_VERTEX, vertex, float("inf"))
        for vertex in sinks:
            self.add_edge(vertex, DEFAULT_END_VIRTUAL_VERTEX, float("inf"))

    def dfs(self, start_node: int, target_node: int, visited: Set[int] = None, path: List[int] = None):
        if visited is None:
            visited = set()
        if path is None:
            path = list()

        visited.add(start_node)
        path.append(start_node)

        if start_node == target_node:
            return path
        for index, capacity in enumerate(self.edges_matrix[start_node]):
            if index not in visited and capacity > 0:
                result_path = self.dfs(index, target_node, visited, path.copy())
                if result_path:
                    return result_path
        return None

    def ford_fulkerson(self, source: str, sink: str) -> int:
        max_flow = 0
        source = self.list_of_vertices.index(source)
        sink = self.list_of_vertices.index(sink)

        path = self.dfs(source, sink)
        while path:
            path_flow = float("Inf")
            for i in range(len(path) - 1):
                current_vertex, next_vertex = path[i], path[i + 1]
                path_flow = min(path_flow, self.edges_matrix[current_vertex][next_vertex])

            for i in range(len(path) - 1):
                current_vertex, next_vertex = path[i], path[i + 1]
                self.edges_matrix[current_vertex][next_vertex] -= path_flow
                self.edges_matrix[next_vertex][current_vertex] += path_flow

            max_flow += path_flow

            path = self.dfs(source, sink)

        return max_flow

    def max_flow(self, sources: list, sinks: list) -> int:
        self.add_virtual_vertexes(sources, sinks)
        return self.ford_fulkerson(DEFAULT_START_VIRTUAL_VERTEX, DEFAULT_END_VIRTUAL_VERTEX)

    def build_graph_from_csv(self):
        with open(self.csv_file, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                self.add_edge(data[0], data[1], int(data[2]))

