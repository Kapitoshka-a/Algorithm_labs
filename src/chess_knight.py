from typing import Tuple

CHESSBOARD = 8


def is_valid(x, y, chessboard=CHESSBOARD):
    return 0 <= x < chessboard and 0 <= y < chessboard


def neighbors(row, col, chessboard=CHESSBOARD):
    rows = [2, 2, -2, -2, 1, 1, -1, -1]
    cols = [-1, 1, 1, -1, 2, -2, 2, -2]
    valid_neighbors = [(rows[i] + row, cols[i] + col) for i in range(chessboard)
                       if is_valid(rows[i] + row, cols[i] + col)]
    return valid_neighbors


def shortest_knight_path(start_position: Tuple[int, int], end_position: Tuple[int, int], chessboard=CHESSBOARD):
    row, col = start_position
    queue = [((row, col), 0)]
    visited = set()

    while queue:
        (row, col), distance = queue.pop(0)
        visited.add((row, col))
        for row, col in neighbors(row, col, chessboard):
            if (row, col) == end_position:
                return distance + 1
            elif (row, col) not in visited:
                queue.append(((row, col), distance + 1))


if __name__ == '__main__':
    print(shortest_knight_path((7, 0), (0, 7)))
