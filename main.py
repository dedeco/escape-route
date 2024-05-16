

"""
Uber Coding Inverview

Escape Route

You're presented with a map like the one below. Imagine you're lost in a land
represented by "1" and surrounded by water ("0").  Your goal is to find the
continuous escape route from the top to the bottom of the map.

m = [ [0, 1, 1, 0],
      [0, 0, 1, 1],
      [1, 1, 1, 1],
      [1, 0, 0, 0]
]

Path Sample:
 [      1,  ],
 [      1,  ],
 [1, 1, 1,  ],
 [1,        ]
"""


dr = [1, 0, 0, -1]
dc = [0, -1, 1, 0]


def is_valid(row, col, matrix, n):
    return 0 <= row < n and 0 <= col < n and matrix[row][col] == 1


def find_path(row, col, matrix, n):
    if row == n - 1 and col in range(0, n):
        return True

    matrix[row][col] = 0

    for i in range(n):

        next_row = row + dr[i]
        next_col = col + dc[i]

        if is_valid(next_row, next_col, matrix, n):
            return find_path(next_row, next_col, matrix, n)

    matrix[row][col] = 1


def find_path_for_every_columns(matrix):
    for i in range(len(matrix)):
        if matrix[0][i] == 1 and find_path(0, i, matrix, len(matrix)):
            return True
    return False


if __name__ == "__main__":

    matriz = [
        [0, 1, 1, 0],
        [0, 0, 1, 1],
        [1, 1, 1, 1],
        [1, 0, 0, 0]
    ]

    assert find_path_for_every_columns(matriz) == True

    # No start point
    matriz = [
        [0, 0, 0, 0],
        [0, 0, 1, 1],
        [1, 1, 1, 1],
        [1, 0, 0, 0]
    ]

    assert find_path_for_every_columns(matriz) == False

    # No path
    matriz = [
        [0, 0, 1, 0],
        [0, 0, 1, 1],
        [1, 1, 0, 0],
        [1, 0, 0, 0]
    ]

    assert find_path_for_every_columns(matriz) == False
