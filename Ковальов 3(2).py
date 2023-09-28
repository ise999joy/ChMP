def f(x):
    return x**4 + 2*x**3 + 2*x**2 + 6*x - 5
def df(x):
    return 4*x**3 + 6*x**2 + 4*x + 6
def combined_method(f, df, a, b, epsilon):
    max_iterations = 1000
    iteration = 0
    while iteration < max_iterations:
        # Метод бісекції
        c = (a + b) / 2
        if abs(f(c)) < epsilon:
            return c
        c = c - f(c) / df(c)

        if abs(f(c)) < epsilon:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        iteration += 1
    return None  # Розв'язок не знайдено
a = 0.0  # Ліва межа інтервалу
b = 2.0  # Права межа інтервалу
epsilon = 0.0001  # Точність
result = combined_method(f, df, a, b, epsilon)
if result is not None:
    print(f"Розв'язок: {result:.4f}")
else:
    print("Не вдалося знайти розв'язок.")
