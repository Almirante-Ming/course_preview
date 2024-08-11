def gerar_dicionario_quadrado(k):
    dicionario_quadrado = {i: i**2 for i in range(1, k + 1)}
    return dicionario_quadrado
k = 15
print(gerar_dicionario_quadrado(k))
