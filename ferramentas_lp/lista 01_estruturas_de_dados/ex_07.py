# Como obter os 3 primeiros e os 3 últimos itens de uma lista juntos? (dica: combine fatiamento com adição)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = lista[:3] + lista[-3:]
print(result)