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
    ['-', '-', '-', '+', '+', '+', '+'],  # 0 3456
    ['-', '-', '+', '+', '+', '+', '+'],  # 1 23456
    ['-', '+', '+', '+', '+', '+', '+'],  # 2 123456
    ['+', '+', '+', '+', '+', '+', '-'],  # 3 012345
    ['+', '+', '+', '+', '+', '-', '-'],  # 4 01234
    ['+', '+', '+', '+', '-', '-', '-'],  # 5 0123
]

diagonals = (
    (3, 4, 5, 6),
    (2, 3, 4, 5, 6),
    (1, 2, 3, 4, 5, 6),
    (0, 1, 2, 3, 4, 5),
    (0, 1, 2, 3, 4),
    (0, 1, 2, 3),
)

diagonal_board = []
for i, t in enumerate(diagonals):
    # print("i: {}, t: {}".format(i, t))
    last = t[-1]
    print("last: ", last)
    if last < 6:
        print(test_board[i][t[0]:last + 1])
        diagonal_board.append(test_board[i][t[0]:last + 1])
    else:
        diagonal_board.append(test_board[i][t[0]:])
        print(test_board[i][t[0]:])

for l in diagonal_board:
    print(l)

# reversed_matrix = [list(val) for val in list(zip(*matrix))]
# for l in matrix:
# print(l)

# for l in reversed_matrix:
# print(l)
