while True:
    B, N = map(int, input().split())
    
    if B == 0 and N == 0:
        break

    reserves = list(map(int, input().split()))

    for _ in range(N):
        D, C, V = map(int, input().split())
        
        D -= 1
        C -= 1
        
        reserves[D] -= V
        reserves[C] += V

    if all(reserve >= 0 for reserve in reserves):
        print("S")
    else:
        print("N")

