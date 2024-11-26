import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    
    H, O = map(int, line.split())
    difference = abs(H - O)
    print(difference)
