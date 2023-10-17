import numpy as np
import matplotlib.pyplot as plt

def f1(x, y):
    return np.cos(x + 0.5) + y - 0.8

def f2(x, y):
    return np.sin(y) - 2 * x - 1.6

x = np.linspace(-5, 5, 400)
y = np.linspace(-5, 5, 400)
X, Y = np.meshgrid(x, y)
Z1 = f1(X, Y)
plt.contour(X, Y, Z1, levels=[0], colors='r')
plt.title('Графік f1(x, y) = 0')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()

Z2 = f2(X, Y)
plt.contour(X, Y, Z2, levels=[0], colors='b')
plt.title('Графік f2(x, y) = 0')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
def simple_iteration(x0, y0, tolerance=1e-3, max_iterations=100):
    x, y = x0, y0
    for i in range(max_iterations):
        x_new = x - f1(x, y)
        y_new = y - f2(x, y)
        if abs(x_new - x) < tolerance and abs(y_new - y) < tolerance:
            return x_new, y_new
        x, y = x_new, y_new
    return None, None

x0 = 1.0
y0 = 1.0
x_sol, y_sol = simple_iteration(x0, y0, tolerance=1e-3)

if x_sol is not None and y_sol is not None:
    print(f'Розв’язок системи: x = {x_sol:.3f}, y = {y_sol:.3f}')
else:
    print('Метод простої ітерації не збігся до розв’язку.')
