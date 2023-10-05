import numpy as np
matrix = np.array([[-1, 2],
                   [0, 1]])

result_matrix = np.linalg.matrix_power(matrix, 2)

print(result_matrix)
