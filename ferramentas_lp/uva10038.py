def is_jolly_jumper(sequence):
    n = sequence[0]  
    numbers = sequence[1:]
    
    if n == 1:
        return "Jolly"
    
    differences = set()
    for i in range(n - 1):
        diff = abs(numbers[i] - numbers[i + 1])
        if 1 <= diff <= n - 1:
            differences.add(diff)
    
    if len(differences) == n - 1:
        return "Jolly"
    else: 
        return "Not jolly"

while True:
    try:
        line = input().strip()
        if not line:
            break
        sequence = list(map(int, line.split()))
        print(is_jolly_jumper(sequence))
    except EOFError:
        break
