def f(x):
    return 6 * x**4 + 8 * x**3 - 24 * x**2 - 7

def df(x):
    return 24 * x**3 + 24 * x**2 - 48 * x

def newton_method(x0, epsilon, max_iterations):
    x = x0
    iteration = 0
    while iteration < max_iterations:
        x_new = x - f(x) / df(x)
        if abs(x_new - x) < epsilon:
            return x_new
        x = x_new
        iteration += 1
    return None

# Використання методу Ньютона для інтервалу [-3, -2]
result3 = newton_method(-3, 0.0001, 100)
print("Результат методу Ньютона на інтервалі [-3, -2]:", result3)

# Використання методу Ньютона для інтервалу [0, 1]
result4 = newton_method(0, 0.0001, 100)
print("Результат методу Ньютона на інтервалі [0, 1]:", result4)
