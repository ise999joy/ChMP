import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

x = np.array([0.1, 0.3, 0.6, 1.1, 1.8])
y = np.array([2.65, 2.75, 2.19, 1.76, 3.43])

cs = CubicSpline(x, y, bc_type='natural')

for i in range(len(x)):
    interpolated_value = cs(x[i])
    original_value = y[i]
    print(f"x={x[i]}, S(x)={interpolated_value}, y={original_value}")

xs = np.linspace(x.min(), x.max(), 100)
ys = cs(xs)

plt.figure()
plt.plot(x, y, 'o', label='Data points')
plt.plot(xs, ys, label='Cubic Spline')
plt.legend()
plt.xlabel('x')
plt.ylabel('Spline Value')
plt.title('Cubic Spline Interpolation')
plt.grid(True)
plt.show()
