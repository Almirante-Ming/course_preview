class ContaBancaria:
    def __init__(self, nome, saldo=0.0):
        self.__nome = nome
        self.__saldo = saldo
        
    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor
        else:
            print("Saldo não pode ser negativo.")

    @property
    def nome(self):
        return self.__nome
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("O valor de depósito deve ser positivo.")
    
    def sacar(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente.")
        else:
            print("O valor de saque deve ser positivo.")
    
    def exibir_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")


class ContaCorrente(ContaBancaria):
    def __init__(self, nome, saldo=0.0, limite_cheque_especial=1000.0):
        super().__init__(nome, saldo)
        self.__limite_cheque_especial = limite_cheque_especial

    @property
    def limite_cheque_especial(self):
        return self.__limite_cheque_especial

    def sacar(self, valor):
        saldo_disponivel = self.saldo + self.limite_cheque_especial
        if valor > 0:
            if valor <= saldo_disponivel:
                novo_saldo = self.saldo - valor
                self.saldo = novo_saldo
                print(f"Saque de R${valor:.2f} realizado com sucesso (Cheque especial utilizado).")
            else:
                print("Saque excede o limite do cheque especial.")
        else:
            print("O valor de saque deve ser positivo.")
    
    def exibir_saldo(self):
        saldo_disponivel = self.saldo + self.limite_cheque_especial
        print(f"Saldo atual: R${self.saldo:.2f}")
        print(f"Saldo disponível (com cheque especial): R${saldo_disponivel:.2f}")


class ContaPoupanca(ContaBancaria):
    def __init__(self, nome, saldo=0.0, taxa_juros=0.05):
        super().__init__(nome, saldo)
        self.__taxa_juros = taxa_juros

    @property
    def taxa_juros(self):
        return self.__taxa_juros

    def aplicar_juros(self):
        juros = self.saldo * self.taxa_juros
        self.saldo += juros
        print(f"Juros de R${juros:.2f} aplicados. Novo saldo: R${self.saldo:.2f}")


c_b = ContaBancaria("Maria", 500.0)
c_b.exibir_saldo()
c_b.depositar(200)
c_b.exibir_saldo()
c_b.sacar(100)
c_b.exibir_saldo()

print("\n--- Conta Corrente ---")
c_c = ContaCorrente("João", 300.0, limite_cheque_especial=500.0)
c_c.exibir_saldo()
c_c.sacar(600)
c_c.exibir_saldo()
c_c.sacar(200)

print("\n--- Conta Poupança ---")
c_p = ContaPoupanca("Ana", 1000.0, taxa_juros=0.02)
c_p.exibir_saldo()
c_p.aplicar_juros()
c_p.exibir_saldo()
