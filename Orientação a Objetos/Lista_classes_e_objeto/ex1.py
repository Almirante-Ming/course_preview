class Data:
    def __init__(self, dia:int, mes:int, ano:int):
        if self.validar(dia, mes, ano):
            self.__dia = dia
            self.__mes = mes
            self.__ano = ano
        else:
            raise ValueError("Dados inválidos.") #sugerido pelo copilot como mais adequado    
    def validar(self, dia:int, mes:int, ano:int) -> bool:
        dias_meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            dias_meses[1] = 29
        if mes >= 1 and mes <= 12:
            if dia >= 1 and dia <= dias_meses[mes-1]:
                return True
            else:
                print("Dia inválido")
        else:
            print("Mês inválido")
        
        return False
    
    def __str__(self):
        return f'{self.__dia}/{self.__mes}/{self.__ano}'

# ---------------------------
d1 = Data(6,4,2001)
d2 = Data(10,2,2024)
d3 = Data(7,10,2001)

print(d1)
print(d2)
print(d3)