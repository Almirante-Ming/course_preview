dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

def juntar_dicionarios(dict1, dict2):
    dicionario_agregado = {**dict1, **dict2}
    return dicionario_agregado

print(juntar_dicionarios(dict1, dict2))
