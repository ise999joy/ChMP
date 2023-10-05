import numpy as np

matrix = np.array([[1, 2, -3],
                   [0, 1, 2],
                   [0, 0, 1]])

inverse_matrix = np.linalg.inv(matrix)

print("Обратная матрица:")
print(inverse_matrix)
