def f(x):
    return 6*x**4 + 8*x**3 - 24*x**2 - 7

def df(x):
    return 24*x**3 + 24*x**2 - 48*x

def newton_method(f, df, x0, tol=1e-4, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            return x
        dfx = df(x)
        if dfx == 0:
            return None  # Збіжність припинена, оскільки похідна дорівнює нулю.
        x = x - fx / dfx
    return None  # Збіжність не досягнута за максимальну кількість ітерацій.

# Початкове наближення
x0 = 1.0

# Виклик методу Ньютона
root = newton_method(f, df, x0)

if root is not None:
    print(f"Корінь рівняння: {root:.4f}")
else:
    print("Метод Ньютона не досягнув збіжності.")
