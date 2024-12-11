# def verificar_ordem(barbas):
#     if barbas == sorted(barbas) or barbas == sorted(barbas, reverse=True):
#         return "Ordered"
#     else:
#         return "Unordered"

# def main():
#     import sys
#     input = sys.stdin.read
#     dados = input().splitlines()
    
#     N = int(dados[0])
#     resultados = ["Lumberjacks:"]
    
#     for i in range(1, N + 1):
#         barbas = list(map(int, dados[i].split()))
#         resultados.append(verificar_ordem(barbas))
    
#     for resultado in resultados:
#         print(resultado)

# if __name__ == "__main__":
#     main()
    
tc = int(input())
print("Lumberjacks:")
for i in range(9):
    lumberjack = input().split()
    
    asc=True
    if int(lumberjack[i]) > int(lumberjack[i+1]):
        asc=False
        break
    
    

