def o_que_faco(n):
    if n == 1 or n == 0:
        return False

    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False

    return True


def numeros(A, B):
    E = 0
    for C in range(A):
        D = int(input())
        if D == B:
            print(E)
            return
        E += D
    print(E)


print(o_que_faco(7))
print(o_que_faco(25))

numeros(10, 80)
