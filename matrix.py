matrix = [
    ['a', 'b', 'c', 'd', 'e', 'f', 'g'],  # 0
    ['A', 'B', 'C', 'D', 'E', 'F', 'G'],  # 1
    ['a', 'b', 'c', 'd', 'e', 'f', 'g'],  # 2
    ['A', 'B', 'C', 'D', 'E', 'F', 'G'],  # 3
    ['a', 'b', 'c', 'd', 'e', 'f', 'g'],  # 4
    ['A', 'B', 'C', 'D', 'E', 'F', 'G'],  # 5
]

# rm = [
#     ('a', 'A', 'a', 'A', 'a', 'A'),
#     ('b', 'B', 'b', 'B', 'b', 'B'),
#     ('c', 'C', 'c', 'C', 'c', 'C'),
#     ('d', 'D', 'd', 'D', 'd', 'D'),
#     ('e', 'E', 'e', 'E', 'e', 'E'),
#     ('f', 'F', 'f', 'F', 'f', 'F'),
#     ('g', 'G', 'g', 'G', 'g', 'G')
# ]

test_board = [
    # 0    1    2    3    4    5    6
    ['-', '-', '-', '0', '1', '2', '3'],  # 0
    ['-', '-', '0', '1', '2', '3', '4'],  # 1
    ['-', '0', '1', '2', '3', '4', '5'],  # 2
    ['0', '1', '2', '3', '4', '5', '-'],  # 3
    ['1', '2', '3', '4', '5', '-', '-'],  # 4
    ['2', '3', '4', '5', '-', '-', '-'],  # 5
]

diagonals = (
    ((3, 0), (2, 1), (1, 2), (0, 3)),
    ((4, 0), (3, 1), (2, 2), (1, 3), (0, 4)),
    ((5, 0), (4, 1), (3, 2), (2, 3), (1, 4), (0, 5)),
    ((6, 0), (5, 1), (4, 2), (3, 3), (2, 4), (1, 5)),
    ((6, 1), (5, 2), (4, 3), (3, 4), (2, 5)),
    ((6, 2), (5, 3), (4, 4), (3, 5)),
)

diagonal_board = []

for t in diagonals:
    # print("i: {}, t: {}".format(i, t))
    new_row = []
    for pos, row in t:
        # print("row: {}, pos: {}".format(row, pos))
        new_row.append(test_board[row][pos])

    diagonal_board.append(new_row)


for l in diagonal_board:
    print(l)

# reversed_matrix = [list(val) for val in list(zip(*matrix))]
# for l in matrix:
# print(l)

# for l in reversed_matrix:
# print(l)
