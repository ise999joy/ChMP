from math import sin

def rectangle_method(func, a, b, n):
    h = (b - a) / n
    result = 0.0
    for i in range(n):
        x = a + i * h
        result += func(x)
    result *= h
    return result

def simpson_method(func, a, b, n):
    h = (b - a) / n
    result = func(a) + func(b)
    for i in range(1, n, 2):
        result += 4 * func(a + i * h)
    for i in range(2, n-1, 2):
        result += 2 * func(a + i * h)
    result *= h / 3
    return result

def trapezoidal_method(func, a, b, n):
    h = (b - a) / n
    result = (func(a) + func(b)) / 2
    for i in range(1, n):
        result += func(a + i * h)
    result *= h
    return result

a1 = 0.4
b1 = 1.2
n1 = 10

def func1(x):
    return 1 / ((0.5 * x + 2) ** 0.5)

result1_rectangle = rectangle_method(func1, a1, b1, n1)
print(f"Результат методом прямокутників для першого інтегралу: {result1_rectangle:.4f}")

a2 = 0.8
b2 = 1.2
n2 = 8

def func2(x):
    return sin(2*x + 1) / x

result2_simpson = simpson_method(func2, a2, b2, n2)
print(f"Результат методом Сімпсона для другого інтегралу: {result2_simpson:.4f}")

a3 = 0.6
b3 = 1.4
n3 = 20

def func3(x):
    return 1 / ((12 * x**2 + 0.5) ** 0.5)

result3_trapezoidal = trapezoidal_method(func3, a3, b3, n3)
print(f"Результат методом трапецій для третього інтегралу: {result3_trapezoidal:.4f}")
