from typing import List, Set, Dict


def dfs(graph: Dict, start, visited: Set = None):
    if visited is None:
        visited = set()
    visited.add(start)

    try:
        for neighbor in graph[start]:
            if neighbor not in visited:
                dfs(graph, neighbor, visited)
    except KeyError:
        return
    return visited


def gas_lines_map(gas_lines: List):
    connections = {}
    for line in gas_lines:
        if line[0] not in connections:
            connections[line[0]] = [line[1]]
        else:
            connections[line[0]].append(line[1])
    return connections


def accessible_cities(gas_stations: List, gas_lines: List):
    gas_ways = {}
    gas_lines_graph = gas_lines_map(gas_lines)

    for gas_station in gas_stations:
        gas_ways[gas_station] = dfs(gas_lines_graph, gas_station)

    return gas_ways


def inaccessible_cities(cities: Set, gas_stations: List, gas_lines: List):
    gas_ways = accessible_cities(gas_stations, gas_lines)
    broken_gas_ways = {}
    for gas_station in gas_ways.keys():
        broken_gas_ways[gas_station] = {city for city in cities if city not in gas_ways[gas_station]}

    return broken_gas_ways


if __name__ == '__main__':
    my_cities = {'A', 'B', 'C', 'D', 'E'}
    my_gas_stations = ['g1', 'g2']
    my_gas_lines = [('g1', 'A'), ('g1', 'B'), ('A', 'D'), ('B', 'D'), ('g2', 'C'), ('C', 'B')]

    print(inaccessible_cities(my_cities, my_gas_stations, my_gas_lines))
