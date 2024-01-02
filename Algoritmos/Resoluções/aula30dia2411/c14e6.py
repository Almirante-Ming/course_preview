import c14e5


# Receber dois naturais e retornar seu MMC, usando a função mmc do exercício anterior como base.
def mmc(a, b):
    return a * b / c14e5.mdc(a, b)


print("digite dois números naturais:")
x = int(input())
y = int(input())
resultado = mmc(x, y)
print(f"o mmc de {x} e {y} é {resultado}")
