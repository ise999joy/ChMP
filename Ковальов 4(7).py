import numpy as np

N = 4
M = 5

A = np.random.rand(N, M)

print("Матриця A:")
print(A)

seredni_rjadky = np.mean(A, axis=1)
seredni_stovptsy = np.mean(A, axis=0)

print("Середні значення для рядків:")
print(seredni_rjadky)
print("Середні значення для стовпців:")
print(seredni_stovptsy)
