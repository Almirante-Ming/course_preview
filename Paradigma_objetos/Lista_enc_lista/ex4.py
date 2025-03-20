def chop(t):
    if len(t) > 1:
        del t[0]
        del t[-1]
    elif len(t) == 1:
        t.clear()  
    return None

t = [1, 2, 3, 4]

print(chop(t))
