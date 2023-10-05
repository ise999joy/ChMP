import numpy as np

A = np.array([[3, 0, 7],
              [-4, 2, 3],
              [-1, 1, 2]])

B = np.array([[1],
              [2],
              [4]])

result = np.dot(A, B)

print(result)
