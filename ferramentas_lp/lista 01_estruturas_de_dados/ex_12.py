# Como obter os 4 itens do meio de uma lista?
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if len(lista) >= 4:
    meio = len(lista) // 2 
    inicio = meio - 2       
    fim = meio + 2          
    result = lista[inicio:fim]
else:
    result = [] 

print(result)
