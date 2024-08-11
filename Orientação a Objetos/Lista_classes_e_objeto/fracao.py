class Fracao:
    def __init__(self, num:int, den:int):
        self.__num=num
        self.__den=den
        
    def __str__(self, num, den):
        f'numerador definido como {num} e denominador {den}'
    
    @property
    def num(self):
        self.__num
    @num.setter
    def num(self, valor):
        self.__num = valor
    
    @property
    def den(self):
        self.__den
    @den.setter
    def den(self, valor):
        self.__den = valor
        
#-------------------------------------------

    def __mul__(self):
        