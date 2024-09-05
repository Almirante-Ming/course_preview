class Temperatura:
    def __init__(self,temp_c:int):
        self.temp_C=temp_c
        
    def __str__(self) -> str:
        return f'temperatura definida em {self.temp_C} graus celsius'
    @staticmethod
    def cff(temp):
        return f'a temperatura em fahrennheint e : {((temp*9/5) + 32)}'
    
    @staticmethod
    def ffc(temp):
        return f'a temperatura em celsius e : {((temp-32)*5/9)}'
    
#-----------------------------------------------
t1=Temperatura(0)
print(t1)
print(Temperatura.cff(25))
print(Temperatura.ffc(32))
