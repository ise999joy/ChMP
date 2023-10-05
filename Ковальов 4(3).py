import numpy as np

matrix = np.array([[2, 3, 4, 1],
                  [1, 2, 3, 4],
                  [3, 4, 1, 2],
                  [4, 1, 2, 3]])

determinant = np.linalg.det(matrix)

print("Визначник матриці:")
print(determinant)
