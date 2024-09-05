class Retangulo:
    lado1=0
    lado2=0
    # def __init__(self, lado1:int, lado2:int):
    #     self.lado1 = lado1
    #     self.lado2 = lado2
        
    def area(self):
        return f'a area do retangulo e : {(Retangulo.lado1)*(Retangulo.lado2)}'
    
    def perimetro(self):
        return f'o perimetro deste retangulo e : {(2*Retangulo.lado1)+(2*Retangulo.lado2)}'
    
    @classmethod
    def set_lados(cls,Nlado1:int,Nlado2:int):
        cls.lado1 = Nlado1
        cls.lado2 = Nlado2 
    
    def __str__(self):
        return f'retangulo({Retangulo.lado1}, {Retangulo.lado2})'
    
#------------------------------
c=Retangulo()
print(c.area())
print(c.perimetro())
print(Retangulo.set_lados(7,9))