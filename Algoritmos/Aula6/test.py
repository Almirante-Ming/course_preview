def contar_multiplos(M, N):
    maior_multiplo=(N//M)*M
    contador=maior_multiplo//M
    return contador

M=int(input("valor de M: "))
N=int(input("valor de N: "))

resultado=contar_multiplos(M, N)
print("o maior multiplo de", M, "menor que ",N, "é:", resultado)