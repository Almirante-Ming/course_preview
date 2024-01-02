# a) Ler uma lista de n itens.
n = int(input("Quantidade de itens:"))
lista = []

print(f"Digite os {n} itens:")
for i in range(n):
    numero = input()
    lista.append(numero)

# b)  Escrever os n itens normalmente em uma linha
print("imprimindo normalmente")
print(lista)

# c) e do último para o primeiro em outra linha.
print("imprimindo de trás para frente")
for i in range(n - 1, -1, -1):
    print(lista[i], end=", ")
