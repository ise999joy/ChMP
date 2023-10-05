import numpy as np

A = np.array([[2, -1, 1],
              [3, 2, 2],
              [1, -2, 1]])
b = np.array([2, -2, 1])
det_A = np.linalg.det(A)
if det_A == 0:
    print("Система не має єдиного розв'язку")
else:
    x_matrix = A.copy()
    x_matrix[:, 0] = b
    x_det = np.linalg.det(x_matrix)

    y_matrix = A.copy()
    y_matrix[:, 1] = b
    y_det = np.linalg.det(y_matrix)

    z_matrix = A.copy()
    z_matrix[:, 2] = b
    z_det = np.linalg.det(z_matrix)
    x = x_det / det_A
    y = y_det / det_A
    z = z_det / det_A
    print(f"x = {x}")
    print(f"y = {y}")
    print(f"z = {z}")
solution = np.linalg.solve(A, b)
print("Розв'язок за допомогою solve():")
print(f"x = {solution[0]}")
print(f"y = {solution[1]}")
print(f"z = {solution[2]}")
