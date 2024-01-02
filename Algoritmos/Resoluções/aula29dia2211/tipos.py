def multiplicar_por_dois(numero):
    return numero * 8

s = "2.7"
f = float(s)
i = int(f)
# i = int(s) # ERRO! não pode!

print(multiplicar_por_dois(i))
print(multiplicar_por_dois(f))
print(multiplicar_por_dois(s))
