import math
class Circulo:
    def __init__(self, raio:float, centro:float=0.0):
        self.__raio = raio
        self.__centro = centro
        
    @property
    def raio(self):
        return self.__raio
    @raio.setter
    def raio(self, valor):
        self.__raio = valor
    
    @property
    def centro(self):
        return self.__centro
    @centro.setter
    def centro(self, valor):
        self.__centro = valor
    
    def __str__(self):
        return f'circulo de raio {self.__raio} na posicao {self.__centro} criado!'
    
    def inflar(self, raio):
        self.__raio+=raio
        return f'o raio foi aumentado em {raio}, valor atual {self.__raio}'
    
    def desinflar(self, raio):
        self.__raio-=raio
        return f'o raio foi diminuido em {raio}, valor atual {self.__raio}'
    
    def mover(self, centro=0.0):
        ca=self.__centro
        cn=centro
        self.__centro = cn
        return f'o centro do circulo foi movido de {ca}, para {cn}'
    
    def area(self, raio:float):
        ar = 3.14 * (raio*raio)
#---------------------------------------------
c1=Circulo(3.14,30)
# print(c1)

# c1.inflar(6.28)
# print(c1)


# c1.desinflar(9)
# print(c1)


# print(c1.centro)
# c1.mover(6.28)
# print(c1.raio)
# print(c1.centro)
c1.area(30)
print(c1.area)