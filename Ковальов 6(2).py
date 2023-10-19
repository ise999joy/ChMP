import numpy as np
import matplotlib.pyplot as plt

x_values = [-1.5, -0.5, 0.5, 2.5]
y_values = [1.5, 2.5, -8.5, 29.5]

def lagrange_interpolation(x, x_values, y_values):
    n = len(x_values)
    result = 0.0

    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if i != j:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term

    return result

x_interp = np.linspace(min(x_values), max(x_values), 400)
y_interp = [lagrange_interpolation(x, x_values, y_values) for x in x_interp]

plt.plot(x_interp, y_interp, label='Інтерполяційна функція', color='blue')
plt.scatter(x_values, y_values, label='Вхідні точки', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Графік інтерполяційної функції')
plt.grid(True)
plt.show()
