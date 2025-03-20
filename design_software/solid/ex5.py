from abc import ABC, abstractmethod

class CapacidadeCarga(ABC):
    @abstractmethod
    def calcular_capacidade_carga(self):
        pass

class Autonomia(ABC):
    @abstractmethod
    def calcular_autonomia(self):
        pass

class DuracaoBateria(ABC):
    @abstractmethod
    def calcular_duracao_bateria(self):
        pass

class Carro(Autonomia, CapacidadeCarga):
    def calcular_capacidade_carga(self):
        return 500

    def calcular_autonomia(self):
        return 600

class Caminhao(Autonomia, CapacidadeCarga):
    def calcular_capacidade_carga(self):
        return 20000

    def calcular_autonomia(self):
        return 1200

class BicicletaEletrica(DuracaoBateria):
    def calcular_duracao_bateria(self):
        return 80

# -------------------------------------------------------
caminhao = Caminhao()
print(caminhao.calcular_capacidade_carga())
