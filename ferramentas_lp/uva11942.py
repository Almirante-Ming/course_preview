def verificar_ordem(barbas):

    if barbas == sorted(barbas) or barbas == sorted(barbas, reverse=True):
        return "Ordered"
    else:
        return "Unordered"

def main():

    N = int(input())
    resultados = ["Lumberjacks:"]
    
    for _ in range(N):
        barbas = list(map(int, input().split()))
        resultados.append(verificar_ordem(barbas))
    
    for resultado in resultados:
        print(resultado)

main()
