alist = [3, 1, 4, 2]
result = alist.sort() 

# O método sort() não retorna nada, ele apenas ordena a lista original.
print(result)
print(alist)

alist = [3, 1, 4, 2]
result = sorted(alist)

# A função sorted() retorna uma nova lista ordenada, sem alterar a lista original.
print(result)
print(alist)