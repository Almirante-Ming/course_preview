from pnrg import prgn, limite #Pseudo Random Generated Number

class Robo:
    def __init__(self, nome:str):
        self.nome = nome
        self.vida = prgn()
        self.nivel_critico=0.3
        
    def __repr__(self):
        return f"Robo(nome={self.nome!r}, vida={self.vida!r})"
    
    def __add__(self, pai):
        mae = self.nome.split('-')[0]
        pai = pai.nome.split('-')[0]
        
        bebe_robo = Robo(f"{mae}-{pai}")
        return bebe_robo
      
    def precisa_medico(self):
        if self.vida < self.nivel_critico:
            return True
        else:
            return False
        
        
class RoboMedico(Robo):
    def __init__(self, nome:str, poder_de_cura:float=prgn()):
        super().__init__(nome)
        self.poder_de_cura = poder_de_cura
            
        pass
    
    def curar(self, Robo:Robo):
        if Robo.precisa_medico() == True:
            Robo.vida += self.poder_de_cura
            return f'{self.nome} curou {Robo.nome} com {self.poder_de_cura} de vida'
        else:
            return f'{Robo.nome} não precisa de cura'
        

class RoboLutador(Robo):
    def __init__(self, nome:str):
        super().__init__(nome)
        self.dano_maximo = 0.7
        self.poder = limite(self.dano_maximo, 1.0)
        
    def atacar(self, robo:Robo):
        dano = round(1-self.poder,3)
        robo.vida -= dano
        if type(robo) == RoboLutador:
            self.vida -= dano
            return f'{self.nome} atacou {robo.nome} com {dano} de dano e sofreu {dano} de dano no combate'
        else:
            return f'{self.nome} atacou {robo.nome} com {dano} de dano'
        