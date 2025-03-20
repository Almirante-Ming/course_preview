class Ponto:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Ponto(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Ponto(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __rmul__(self, scalar):
        return Ponto(scalar * self.x, scalar * self.y)


p1 = Ponto(2, 3)
p2 = Ponto(4, 5)

print(f"P1: {p1}")

p3 = p1 + p2
print(f"P1 + P2 = {p3}")

p4 = p1 - p2
print(f"P1 - P2 = {p4}")

produto_escalar = p1 * p2
print(f"P1 * P2 (produto escalar) = {produto_escalar}")

p5 = 3 * p1
print(f"3 * P1 = {p5}")
