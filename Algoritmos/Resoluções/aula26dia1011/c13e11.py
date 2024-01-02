# Ler um natural n, indicando a capacidade máxima de itens em uma lista, seguido por uma série de duplas i e x. Cada dupla representa um índice i e seu respectivo item x na lista. Encerrar a leitura ao encontrar um índice inválido. Caso não seja fornecido um determinado índice, considerar seu item como zero. Escrever a lista resultante.

n = int(input("digite o tamanho da lista: "))

lista = []
for i in range(n):
    lista.append(0)

while True:
    i = int(input("digite o índice: "))
    if i >= n or i < 0:
        print("índice inválido! encerrando a leitura...")
        break
    x = int(input("digite o item: "))

    lista[i] = x

print("a lista resultante é:")
print(lista)
