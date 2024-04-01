from typing import Tuple


def is_valid(x, y):
    return 0 <= x < 8 and 0 <= y < 8


def neighbors(row, col):
    rows = [2, 2, -2, -2, 1, 1, -1, -1]
    cols = [-1, 1, 1, -1, 2, -2, 2, -2]
    valid_neighbors = [(rows[i] + row, cols[i] + col) for i in range(8)
                       if is_valid(rows[i] + row, cols[i] + col)]
    return valid_neighbors


def shortest_knight_path(start_position: Tuple[int, int], end_position: Tuple[int, int]):
    row, col = start_position
    queue = [((row, col), 0)]
    visited = set()

    while queue:
        (row, col), distance = queue.pop(0)
        visited.add((row, col))
        for row, col in neighbors(row, col):
            if (row, col) == end_position:
                return distance + 1
            elif (row, col) not in visited:
                queue.append(((row, col), distance + 1))


if __name__ == '__main__':
    print(shortest_knight_path((7, 0), (0, 7)))
