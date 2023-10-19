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

x_values = [-2, 0, 1, 2]
y_values = [-11, -3, -11, 5]

points_to_evaluate = [-1.5,-0.5,0.5,2.5]

for x in points_to_evaluate:
    result = lagrange_interpolation(x, x_values, y_values)
    print(f"f({x}) = {result:.3f}")
