import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
    
def original_function(x):
    return np.exp(-x) + x**2

x_data = np.array([1, 2, 3, 4, 5])
y_data = original_function(x_data)

def linear_fit(x, m, b):
    return m * x + b

def quadratic_fit(x, a, b, c):
    return a * x**2 + b * x + c

linear_params, _ = curve_fit(linear_fit, x_data, y_data)
m, b = linear_params

quadratic_params, _ = curve_fit(quadratic_fit, x_data, y_data)
a, b, c = quadratic_params

x_range = np.linspace(min(x_data), max(x_data), 100)

plt.scatter(x_data, y_data, label='Точки')
plt.plot(x_range, original_function(x_range), label='Оригінальна функція')
plt.plot(x_range, linear_fit(x_range, m, b), label='Апроксимація прямою')
plt.plot(x_range, quadratic_fit(x_range, a, b, c), label='Апроксимація параболою')

plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Апроксимація методом найменших квадратів')
plt.show()
