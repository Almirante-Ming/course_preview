import sys
for linha in sys.stdin:
    v, t = map(int, linha.split())
    print(2 * v * t)
