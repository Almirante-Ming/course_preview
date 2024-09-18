from pnrg import attr, limite

class Robo:
    nivel_critico = 0.3  

    def __init__(self, nome: str):
        self.nome = nome
        self.vida = attr()
    
    def __repr__(self):
        return f"Robo(nome={self.nome!r}, vida={self.vida!r})"

    def __add__(self, outro_robo):
        mae = self.nome.split('-')[0]
        pai = outro_robo.nome.split('-')[0]
        return type(self)(f"{mae}-{pai}")
    
    def precisa_de_medico(self):
        return self.vida < self.nivel_critico


class RoboMedico(Robo):
    def __init__(self, nome: str):
        super().__init__(nome)
        self.poder_de_cura = attr()
    
    def curar(self, robo: Robo):
        if robo.precisa_de_medico() and self.vida >= robo.vida:
            cura = min(1 - robo.vida, self.poder_de_cura)
            robo.vida += cura
            robo.vida = round(robo.vida, 3)
            return f'{self.nome} curou {robo.nome} com {cura:.3f} de vida. Vida atual de {robo.nome}: {robo.vida:.3f}'
        elif robo.precisa_de_medico():
            return f'{self.nome} tentou curar {robo.nome} mas não conseguiu'
        else:
            return f'{robo.nome} não precisa de cura'


class RoboLutador(Robo):
    dano_maximo = 0.7

    def __init__(self, nome: str):
        super().__init__(nome)
        self.poder = limite(self.dano_maximo, 1.0)

    def atacar(self, robo: Robo):
        if robo.vida == 0.000:
            return f'{robo.nome} já está fora de combate!'

        dano = round(1 - self.poder, 3)
        robo.vida -= dano
        robo.vida = max(round(robo.vida, 3), 0)
        
        resultado = f'{self.nome} atacou {robo.nome} com {dano:.3f} de dano. Vida de {robo.nome}: {robo.vida:.3f}'

        if type(robo) == RoboLutador and robo.vida > 0:
            dano_contra = round(1 - robo.poder, 3)
            
            if self.vida > 0:
                self.vida -= dano_contra
                self.vida = max(round(self.vida, 3), 0)
                resultado += f' {robo.nome} contra-atacou com {dano_contra:.3f} de dano. Vida de {self.nome}: {self.vida:.3f}'
        
        return resultado
