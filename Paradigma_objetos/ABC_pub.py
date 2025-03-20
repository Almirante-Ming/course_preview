from abc import ABC, abstractmethod

class Publicacao(ABC):
    def __init__(self, titulo:str, autor:str):
        self.titulo=titulo
        self.autor=autor
    
    @abstractmethod
    def info(self, titulo, autor):
        pass
#--------------------------------------------------------

class Livro(Publicacao):
    def __init__(self, titulo:str, autor:str, numPag:int):
        super().__init__(titulo, autor)
        self.numPag = numPag
    
    def info(self,titulo,autor,numPag):
        print(f"o livro {titulo}, foi escrito por {autor} e possui {numPag} Paginas")
#-----------------------------------------------------------

class Artigo(Publicacao):
    def __init__(self, titulo:str, autor:str, revista:str):
        super().__init__(titulo,autor)
        self.revista = revista
    
    def info(self, titulo, autor, revista):
        print(f"o artigo {titulo}, foi escrito por {autor} e publicado na revista {revista}")
        
#----------------------------------------------------------

class Revista(Publicacao):
    def __init__(self, titulo:str, autor:str, edicao:int):
        super().__init__(titulo,autor)
        self.edicao = edicao
    
    def info(self, titulo, autor, edicao):
        print(f"revista: {titulo}, foi escrito por {autor}, edicao {edicao}")
            
