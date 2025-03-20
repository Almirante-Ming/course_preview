from abc import ABC, abstractmethod
class Veiculo(ABC):
    def __init__(self, velocidade:int=0, marca:str=''):
        self.velocidade = velocidade
        self.marca=marca
    
    @abstractmethod
    def mover(self, metros:int):
        pass
    

class Carro(Veiculo):
    def __init__(self, marca:str='',velocidade:int=0, numPortas:int=0):
        super().__init__(velocidade, marca)
        self.numPortas = numPortas
    
    def mover(self, metros: int):
        print(f"o carro moveu {metros} metros")