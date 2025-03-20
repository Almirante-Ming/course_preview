class Brinquedo:
    def __init__(self, velocidade:float|int = 0 ,aceleracao:float|int=0):
        self.__velocidade = velocidade
        self.__aceleracao = aceleracao
    
    def mover(self, velocidade, acelecao):
        print(f"o brinquedo se moveu com velocidade {velocidade} e aceleracao {acelecao}")

class Carro(Brinquedo):
    def mover(self, velocidade, acelecao):
        print(f"o carro se moveu a {velocidade} e com aceleracao {acelecao}")
    




a=Brinquedo(0,0)
a.mover(27, 18)
a.mover(36, 28)

b=Carro(velocidade=0,aceleracao=0)
b.mover(23,77)