qtd = 10
nomes = ["maria", "ana", "francisca", "antonia", "adriana", "jose", "joao", "antonio", "francisco", "luiz"]

print("Nomes:", nomes)

print("\nAlterando...\n")

for i in range(qtd):
    nomes[i] = nomes[i].upper()

print("Nomes alterados:", nomes)
