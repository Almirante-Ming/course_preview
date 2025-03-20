while True:
    try:
        line = input().strip()
        if not line:
            continue
        
        H, O = map(int, line.split())
        difference = abs(H - O)
        print(difference)
    except EOFError:
        break