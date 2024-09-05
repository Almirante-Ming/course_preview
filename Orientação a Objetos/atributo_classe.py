class Conta:
    _total_contas = 0
    def __init__(self):
      Conta._total_contas+=1
      
    @classmethod
    def get_total_contas(cls):
        Conta._total_contas