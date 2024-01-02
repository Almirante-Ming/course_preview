# Para construir um triângulo é necessário que a medida de qualquer um dos lados seja menor que a soma das medidas dos outros dois. Receber três números, e retornar true caso eles formem um triângulo válido, ou false, caso contrário.


def eh_triangulo(a, b, c):
    if a >= b + c:
        return False
    if b >= a + c:
        return False
    if c >= b + a:
        return False
    return True


print("digite três lados para formar um triângulo...")
lado1 = float(input())
lado2 = float(input())
lado3 = float(input())

if eh_triangulo(lado1, lado2, lado3):
    print("triângulo válido!")
else:
    print("você não informou lados válidos...")
