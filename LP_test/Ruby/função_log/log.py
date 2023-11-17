import math
import matplotlib.pyplot as plt


l=float(input("digite o valor do logaritimando: "))
b=float(input("digite o valor da base: "))

if l > 0 and l != 1:
    res = math.log(l, b)
    print("o logarítmo de {l}, na base {b}, é: {res}")
else:
    print("digite valores válidos !!!")
    