conjunto = 1
while True:
    n = int(input().strip())
    if n == 0:
        break
    pilhas = list(map(int, input().strip().split()))
    altura_total = sum(pilhas)
    altura_media = altura_total // n

    movimentos = 0
    for altura in pilhas:
        if altura > altura_media:
            movimentos += altura - altura_media

    print(f"Set #{conjunto}")
    print(f"The minimum number of moves is {movimentos}.")
    print("")
    conjunto += 1
