import numpy as np

matrix = np.array([
    [-2, 3, 1, -1],
    [3, 2, 1, 4],
    [1, 2, 3, 4],
    [0, 2, 3, 3]
])

rank = np.linalg.matrix_rank(matrix)

print(f'Ранг матриці: {rank}')
