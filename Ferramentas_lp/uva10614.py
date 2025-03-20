import math

def numero_de_filas(n):
    if n == 0:
        return 0

    k = int((-1 + math.sqrt(1 + 8 * n)) // 2)

    soma_k = k * (k + 1) // 2
    if soma_k == n:
        return k
    elif soma_k < n:
        return k + 1
    else:
        return k

t = int(input())
for _ in range(t):
    n = int(input())
    print(numero_de_filas(n))