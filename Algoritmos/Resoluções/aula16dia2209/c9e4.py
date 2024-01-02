# Dado um número, ele é múltiplo de 3 ou 5, mas não simultaneamente pelos dois?

# 15 é multiplo de 3 de 5, logo, a resposta é não

# 18 e múltiplo apenas de 3, logo, é sim

# 20 é múltiplo apenas de 5, logo, e sim tbm

# 30 é multiplo de 3 e de 5, logo é nao

# 17 nao é múltiplo de ninguém, logo é não

x = int(input())

if x % 3 == 0 and x % 5 == 0:
    print("NÃO")
elif x % 3 != 0 and x % 5 != 0:
    print("NÃO")
else:
    print("SIM")
