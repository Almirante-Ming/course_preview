class Ponto2D:
    def __init__(self, X:float=0.0, Y:float=0.0):
        self.__X = X
        self.__Y = Y
        
    @property
    def X(self):
        return self.__X
    @X.setter
    def X(self, valor):
        self.__X = valor
    
    @property
    def Y(self):
        return self.__Y 
    @Y.setter
    def Y(self, valor):
        self.__Y = valor
        
    def compara(self, X, Y):
        if X == self.__X and Y == self.__Y:
            return True
        else:
            return False
        
    def __str__(self):
        return f'coordenadas X={self.__X} e Y={self.__Y} registradas!'
    
    def calcRange(self, X2:float, Y2:float):
        X=self.__X
        Y=self.__Y
        x=X-X2
        y=Y-Y2
        r = f'a diferenca e de {abs(x)}, para X e {abs(y)}, para Y.'
        return r
        
    def clone(self):
        nx=self.__X
        ny=self.__Y
        NI=Ponto2D(nx, ny)
        return NI
        
        
#----------------------------------------
# cria uma instancia do objeto
# c1=Ponto2D(1.2,2.3)
# print(c1)

# compara
# cc=c1.compara(1.0,2.0)
# print(cc)

# afere a diferenca dos valores
# cr=c1.calcRange(4.4,4.6)
# print(cr)

# clona o objeto, mantendo seus dados
# ck=c1.clone()
# print(ck)