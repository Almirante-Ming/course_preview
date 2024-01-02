# Ler uma lista de n itens, seguida por uma sequência de itens que se encerra com um item ausente na lista. Para cada item, substituir sua primeira ocorrência na lista por zero. Escrever a lista resultante.

n = int(input("quantos amigos vc quer adicionar na tua lista? "))

amigos = []
print(f"ótimo, agora digite o nome de seus {n} amigos:")
for i in range(n):
    amigo = input()
    amigos.append(amigo)

print("ok, agora digite os amigos que você quer remover da tua lista:")
continuar = True
while continuar:
    continuar = False
    ex_amigo = input()
    for i in range(n):
        if amigos[i] == ex_amigo:
            amigos[i] = 0
            continuar = True
            print(f"{ex_amigo} excluído da tua lista!")
            break
print("tua lista de amigos resultante é:")
print(amigos)
