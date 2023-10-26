import numpy as np

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

x_points = [0.122, 0.129, 0.117, 0.146, 0.157, 0.167]

for x in x_points:
    y = interpolate_newton(x, x_values, y_values)
    print(f"f({x}) = {y}")
