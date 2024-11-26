alist = [3, 1, 4, 2]
result = alist.reverse()

# O método reverse() não retorna nada, ele apenas inverte a lista original.
print(result)
print(alist)

alist = [3, 1, 4, 2]
result = reversed(alist)

# A função reversed() retorna um iterador que inverte a lista original.
print(list(result)) # list() Converte o iterador para uma lista.
print(alist)