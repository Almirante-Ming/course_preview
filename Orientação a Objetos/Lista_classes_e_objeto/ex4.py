class Pais:
    def __init__(self, iso:int,nome:str, extensao:int, populacao:int,limites):
        self.__iso = iso
        self.__nome = nome
        self.__extensao = extensao
        self.__populacao = populacao
        self.limites = limites
    
    @property
    def iso(self):
        return self.__iso
    @iso.setter
    def iso(self, value):
        self.__iso = value
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, value):
        self.__nome = value
    @property
    def extensao(self):
        return self.__extensao
    @extensao.setter
    def extensao(self, value):
        self.__extensao = value
    @property
    def populacao(self):
        return self.__populacao    
    @populacao.setter
    def populacao(self, value):
        self.__populacao = value
        
#--------------------------------------
    def compara(self, ic:int):
        if ic == self.__iso:
            return f"os codigos respresenta o mesmo pais !"
        else:
            return f"os codigos representam diferentes paises !"
           
           
    def divisa(self, destino):
        c=0
        while c < len(self.limites):
            if self.limites[c] == destino:
                return f'este pais faz fronteira com o destinatario'
            elif c == len(self.limites):
                return f'o pais atual nao faz fronteira com o destinatario'
            else:
                c+=1
         
         
    def densidade(self):
       return f'a densidade populacional e de {(self.__populacao/self.__extensao)} por Km2'
   
   
    def vizinhos(self, pais_comparar):
       c=0
       while c < len(self.limites):
           if self.limites[c] == pais_comparar:
               return f'o pais atual tem a fronteira em comum com {self.limites[c]}'
           elif c == len(self.limites):
               return f'o pais nao possui fronteira em comum'
           else:
               c+=1
        
        
# bra=Pais(190,"brasil",123,987,['paraguai', 'bolivia'])
# eua=Pais(191,"estados unidos",321,789,['canada','mexico'])

# print(bra.compara(eua.iso))     
# print(bra.densidade())