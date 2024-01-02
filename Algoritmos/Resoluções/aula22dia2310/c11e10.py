orig = int(input())
inv = 0
while orig != 0:
    resto = orig % 10
    inv = inv * 10 + resto
    orig = orig // 10
print(inv)
