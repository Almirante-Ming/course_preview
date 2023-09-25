c1 = "d"
c2 = "h"
n1 = 7

c3 = chr(n1 + ord(c1))
print(n1, "letras depois de", c1, "é", c3)

n2 = ord(c2) - ord(c1) - 1
print("há", n2, "letras entre", c1, "e", c2)

c4 = ord(c1) * ord(c2)
print(c1, "*", c2, "=", c4)

n3 = ord(c1) + ord(c2)
print(c1, "+", c2, "=", n3)