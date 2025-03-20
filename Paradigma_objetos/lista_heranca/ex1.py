class Funcionario:
    def __init__(self, nome, cpf, salario, departamento):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.departamento = departamento
    
    @classmethod
    def bonificar(cls, funcionario):
        funcionario.salario *= 1.10

    def __str__(self):
        return f"Funcionário: {self.nome}, CPF: {self.cpf}, Salario: {self.salario:.2f}, Departamento: {self.departamento}"


class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, departamento, senha, num_funcionarios):
        super().__init__(nome, cpf, salario, departamento)
        self.senha = senha
        self.num_funcionarios = num_funcionarios

    @classmethod
    def bonificar(cls, gerente):
        gerente.salario *= 1.15

    def autenticar_senha(self, senha):
        if self.senha == senha:
            print('autenticado com sucesso')
            return True
        else:
            print('senha incorreta')
            return False

    def __str__(self):
        return (f"Gerente: {self.nome}, CPF: {self.cpf}, Salário: {self.salario:.2f}, "
                f"Departamento: {self.departamento}, Funcionários gerenciados: {self.num_funcionarios}")




funcionario = Funcionario("Carlos Silva", "123.456.789-00", 3000, "Vendas")
print(funcionario)
Funcionario.bonificar(funcionario)
print(f"Após bonificação: {funcionario}")

gerente = Gerente("Ana Souza", "987.654.321-00", 5000, "TI", "senha123", 5)
print(gerente)
Gerente.bonificar(gerente)
print(f"Após bonificação: {gerente}")

senha_correta = gerente.autenticar_senha("senha123")
senha_incorreta = gerente.autenticar_senha("senhaerrada")
print(f"Senha correta: {senha_correta}")
print(f"Senha incorreta: {senha_incorreta}")  
