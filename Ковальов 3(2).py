def f(x):
    return 6 * x**4 + 8 * x**3 - 24 * x**2 - 7

def df(x):
    return 24 * x**3 + 24 * x**2 - 48 * x

def combined_method(a, b, epsilon):
    while (b - a) >= epsilon:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

# Використання комбінованого методу для інтервалу [-3, -2]
result1 = combined_method(-3, -2, 0.0001)
print("Результат комбінованого методу на інтервалі [-3, -2]:", result1)

# Використання комбінованого методу для інтервалу [0, 1]
result2 = combined_method(0, 1, 0.0001)
print("Результат комбінованого методу на інтервалі [0, 1]:", result2)
