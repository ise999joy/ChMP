import numpy as np

matrix = np.array([[2, 4, 5],
                  [1, 1, 2],
                  [2, 4, 3]])

determinant = np.linalg.det(matrix)

print("Определитель матрицы:")
print(determinant)
