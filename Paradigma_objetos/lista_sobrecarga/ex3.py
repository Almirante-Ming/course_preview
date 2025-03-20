from datetime import datetime

class Relogio:
    def __init__(self, horas=None, minutos=None, segundos=None):
        agora = datetime.now()
    
        self.horas = horas if horas is not None else agora.hour
        self.minutos = minutos if minutos is not None else agora.minute
        self.segundos = segundos if segundos is not None else agora.second

        if not (0 <= self.horas < 24):
            print("Hora inválida")
            self.horas = 0

        if not (0 <= self.minutos < 60):
            print("Minuto inválido")
            self.minutos = 0

        if not (0 <= self.segundos < 60):
            print("Segundo inválido")
            self.segundos = 0

    def __repr__(self):
        return f"{self.horas:02}:{self.minutos:02}:{self.segundos:02}"

    def __add__(self, other):
        segundos_totais = self.segundos + other.segundos
        minutos_totais = self.minutos + other.minutos + (segundos_totais // 60)
        horas_totais = self.horas + other.horas + (minutos_totais // 60)
        
        segundos_totais %= 60
        minutos_totais %= 60
        horas_totais %= 24

        return Relogio(horas_totais, minutos_totais, segundos_totais)

    def __sub__(self, other):
        if self < other:
            print("O primeiro horário deve ser maior que o segundo")
            return None

        segundos_totais = self.segundos - other.segundos
        minutos_totais = self.minutos - other.minutos
        horas_totais = self.horas - other.horas

        if segundos_totais < 0:
            segundos_totais += 60
            minutos_totais -= 1
        if minutos_totais < 0:
            minutos_totais += 60
            horas_totais -= 1
        if horas_totais < 0:
            horas_totais += 24

        return Relogio(horas_totais, minutos_totais, segundos_totais)

    def __eq__(self, other):
        return (self.horas == other.horas and
                self.minutos == other.minutos and
                self.segundos == other.segundos)

    def __gt__(self, other):
        return (self.horas, self.minutos, self.segundos) > (other.horas, other.minutos, other.segundos)

    def __lt__(self, other):
        return (self.horas, self.minutos, self.segundos) < (other.horas, other.minutos, other.segundos)

r0 = Relogio(16, 61, 54)
r1 = Relogio(18, 37, 32)
r2 = Relogio(20, 0, 30)
r_atual = Relogio()

print(r1)
print(r2)
print(r_atual)

r3 = r1 + r2
print(r3) 
r4 = r3 - r2 
print(r4)  

r4 = r2 - r3
print(r4)  

print(r1 == r2) 
print(r1 == Relogio(18, 37, 32))  
print(r3 > r3)  
print(r3 > r2)  
print(r2 > r3)  
print(r1 < r2)  
