class Graph:
    def __init__(self, vertices: int = 10):
        self.map_of_vertices = []
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v, c):
        if u not in self.map_of_vertices:
            self.map_of_vertices.append(u)
        if v not in self.map_of_vertices:
            self.map_of_vertices.append(v)
        self.adj_matrix[self.map_of_vertices.index(u)][self.map_of_vertices.index(v)] = c

    def dfs(self, start_node, target_node, visited=None, path=None):
        if visited is None:
            visited = set()
        if path is None:
            path = list()

        visited.add(start_node)
        path.append(start_node)

        if start_node == target_node:
            return path
        for ind, capacity in enumerate(self.adj_matrix[start_node]):
            if ind not in visited and capacity > 0:
                result_path = self.dfs(ind, target_node, visited, path.copy())
                if result_path:
                    return result_path
        return None

    def ford_fulkerson(self, source, sink):
        max_flow = 0
        source = self.map_of_vertices.index(source)
        sink = self.map_of_vertices.index(sink)

        path = self.dfs(source, sink)
        while path:
            path_flow = float("Inf")
            for i in range(len(path) - 1):
                u, v = path[i], path[i + 1]
                path_flow = min(path_flow, self.adj_matrix[u][v])

            for i in range(len(path) - 1):
                u, v = path[i], path[i + 1]
                self.adj_matrix[u][v] -= path_flow
                self.adj_matrix[v][u] += path_flow

            max_flow += path_flow

            path = self.dfs(source, sink)

        return max_flow

    def build_graph_from_csv(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                self.add_edge(data[0], data[1], int(data[2]))
        return self.adj_matrix


graph = Graph()
graph.add_edge("F1", "F2", 10)
graph.add_edge("F2", "S1", 5)
graph.add_edge('F2', 'S1', 8)
graph.add_edge('S2', 'S3', 12)
graph.add_edge('S3', 'F2', 6)
graph.add_edge('F2', 'S4', 15)
graph.add_edge('F3', 'S5', 7)

print(graph.ford_fulkerson("F1", "S4"))

