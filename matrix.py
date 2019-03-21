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

b2t_board = [
    # 0    1    2    3    4    5    6
    ['-', '-', '-', '0', '1', '2', '3'],  # 0
    ['-', '-', '0', '1', '2', '3', '4'],  # 1
    ['-', '0', '1', '2', '3', '4', '5'],  # 2
    ['0', '1', '2', '3', '4', '5', '-'],  # 3
    ['1', '2', '3', '4', '5', '-', '-'],  # 4
    ['2', '3', '4', '5', '-', '-', '-'],  # 5
]

b2t_diagonals = (
    ((3, 0), (2, 1), (1, 2), (0, 3)),
    ((4, 0), (3, 1), (2, 2), (1, 3), (0, 4)),
    ((5, 0), (4, 1), (3, 2), (2, 3), (1, 4), (0, 5)),
    ((5, 1), (4, 2), (3, 3), (2, 4), (1, 5), (0, 6)),
    ((5, 2), (4, 3), (3, 4), (2, 5), (1, 6)),
    ((5, 3), (4, 4), (3, 5), (2, 6)),
)

t2b_board = [
    ['3', '2', '1', '0', '-', '-', '-'],
    ['4', '3', '2', '1', '0', '-', '-'],
    ['5', '4', '3', '2', '1', '0', '-'],
    ['-', '5', '4', '3', '2', '1', '0'],
    ['-', '-', '5', '4', '3', '2', '1'],
    ['-', '-', '-', '5', '4', '3', '2']
]

# Tuples containing (row, position) of diagonal lines, top to bottom a.k.a. t2b
t2b_diagonals = (
    ((2, 0), (3, 1), (4, 2), (5, 3)),
    ((1, 0), (2, 1), (3, 2), (4, 3), (5, 4)),
    ((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)),
    ((0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)),
    ((0, 2), (1, 3), (2, 4), (3, 5), (4, 6)),
    ((0, 3), (1, 4), (2, 5), (3, 6)),
)


computed_board1 = []

for t in b2t_diagonals:
    new_row = []
    for row, pos in t:
        # print("row: {}, pos: {}".format(row, pos))
        new_row.append(b2t_board[row][pos])

    computed_board1.append(new_row)


for l in computed_board1:
    print(l)


computed_board2 = []

for t in t2b_diagonals:
    new_row = []
    for row, pos in t:
        # print("row: {}, pos: {}".format(row, pos))
        new_row.append(t2b_board[row][pos])
    computed_board2.append(new_row)

for l in computed_board2:
    print(l)
# reversed_matrix = [list(val) for val in list(zip(*matrix))]
# for l in matrix:
# print(l)

# for l in reversed_matrix:
# print(l)
