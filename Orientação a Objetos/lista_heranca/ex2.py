from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    def __init__(self):
        self.area = 0
        self.perimetro = 0

    @abstractmethod
    def calcula_area(self):
        pass
    
    @abstractmethod
    def calcula_perimetro(self):
        pass


class Retangulo(FormaGeometrica):
    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura
    
    def calcula_area(self):
        self.area = self.base * self.altura
        return self.area
    
    def calcula_perimetro(self):
        self.perimetro = 2 * (self.base + self.altura)
        return self.perimetro


class Triangulo(FormaGeometrica):
    def __init__(self, lado1, lado2, lado3):
        super().__init__()
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def calcula_area(self):
        s = (self.lado1 + self.lado2 + self.lado3) / 2
        self.area = (s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3)) ** 0.5
        return self.area
    
    def calcula_perimetro(self):
        self.perimetro = self.lado1 + self.lado2 + self.lado3
        return self.perimetro


retangulo = Retangulo(5, 10)
print(f"Área do Retângulo: {retangulo.calcula_area():.2f}")
print(f"Perímetro do Retângulo: {retangulo.calcula_perimetro():.2f}")

triangulo = Triangulo(3, 4, 5)
print(f"Área do Triângulo: {triangulo.calcula_area():.2f}")
print(f"Perímetro do Triângulo: {triangulo.calcula_perimetro():.2f}")

print(f"O retângulo é uma instância de FormaGeometrica? {isinstance(retangulo, FormaGeometrica)}")
print(f"O triângulo é uma instância de FormaGeometrica? {isinstance(triangulo, FormaGeometrica)}")
