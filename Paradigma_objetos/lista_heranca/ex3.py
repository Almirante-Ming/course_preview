class Atleta:
    def __init__(self, peso):
        self.aposentado = False
        self.peso = peso

    def aposentar(self):
        self.aposentado = True
        print(f"O atleta foi aposentado.")

    def aquecer(self):
        print(f"O atleta está aquecendo.")


class Corredor(Atleta):
    def correr(self):
        print("O corredor está correndo.")


class Nadador(Atleta):
    def nadar(self):
        print("O nadador está nadando.")


class Ciclista(Atleta):
    def pedalar(self):
        print("O ciclista está pedalando.")


class TriAtleta(Corredor, Nadador, Ciclista):
    pass


tri_atleta = TriAtleta(peso=70)
tri_atleta.aquecer()
tri_atleta.correr()
tri_atleta.nadar()
tri_atleta.pedalar()
tri_atleta.aposentar()
