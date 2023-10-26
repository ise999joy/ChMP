import numpy as np
import matplotlib.pyplot as plt

x_values = [0.115, 0.120, 0.125, 0.130, 0.135, 0.140, 0.145, 0.150, 0.155, 0.160, 0.165]
y_values = [8.6572, 8.2932, 7.9582, 7.6489, 7.3623, 7.0961, 6.8491, 6.6185, 6.3998, 6.1965, 6.0055]

def interpolate_newton(x, x_values, y_values):
    n = len(x_values)
    result = 0
    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if j != i:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term
    return result

x_interp = np.linspace(min(x_values), max(x_values), 100)
y_interp = [interpolate_newton(x, x_values, y_values) for x in x_interp]

plt.figure(figsize=(8, 6))
plt.scatter(x_values, y_values, label='Задані значення', color='red', marker='o')
plt.plot(x_interp, y_interp, label='Інтерполяційна функція', color='blue')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.title('Графік інтерполяційної функції')
plt.show()
