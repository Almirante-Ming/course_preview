amostra_dicionario = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}
chaves = ["name", "salary"]

def extrair(amostra_dicionario, chaves):
    extracted_dict = {chave: amostra_dicionario[chave] for chave in chaves if chave in amostra_dicionario}
    return extracted_dict

result = extrair(amostra_dicionario, chaves)
print(result)
