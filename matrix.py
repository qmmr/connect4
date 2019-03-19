matrix = [
    ['a', 'b', 'c', 'd', 'e', 'f', 'g'],  # 0
    ['A', 'B', 'C', 'D', 'E', 'F', 'G'],  # 1
    ['a', 'b', 'c', 'd', 'e', 'f', 'g'],  # 2
    ['A', 'B', 'C', 'D', 'E', 'F', 'G'],  # 3
    ['a', 'b', 'c', 'd', 'e', 'f', 'g'],  # 4
    ['A', 'B', 'C', 'D', 'E', 'F', 'G'],  # 5
]

rm = [
    ('a', 'A', 'a', 'A', 'a', 'A'),
    ('b', 'B', 'b', 'B', 'b', 'B'),
    ('c', 'C', 'c', 'C', 'c', 'C'),
    ('d', 'D', 'd', 'D', 'd', 'D'),
    ('e', 'E', 'e', 'E', 'e', 'E'),
    ('f', 'F', 'f', 'F', 'f', 'F'),
    ('g', 'G', 'g', 'G', 'g', 'G')
]

reversed_matrix = [list(val) for val in list(zip(*matrix))]
for l in matrix:
    print(l)

for l in reversed_matrix:
    print(l)
