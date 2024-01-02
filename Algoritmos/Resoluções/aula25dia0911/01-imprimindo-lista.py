qtd = 10  # comprimento da lista
nomes = ["maria", "ana", "francisca", "antonia", "adriana", "jose", "joao", "antonio", "francisco", "luiz"]

print("\nImprimindo item por item:")

print("\n\nImprimindo item por item personalizadamente:")
print(nomes[0], end=", ")
for i in range(1, qtd - 2):
    print(nomes[i], end=", ")
print(nomes[qtd - 2] + " e " + nomes[qtd - 1])
