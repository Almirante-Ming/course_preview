class Cadastro:
    def __init__(self, login, senha):
        self.__login = login
        self.__senha = senha

    @property
    def login(self):
        return self.__login
    @login.setter
    def login(self):
        self.__login.len(15)

    @property
    def senha(self):
        return self.__senha
    @senha.setter
    def senha(self):
        self.__senha.len(8)
    

        