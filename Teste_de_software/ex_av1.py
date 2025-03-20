# leia duas notas bimestrais e informe "aprovado" se a média for maior ou igual a 6,0, exame para 3 e 5,9 e "reprovado" abaixo de 3.


# media = (n1 + n2) / 2

# if media >= 6:
#     print("Aprovado")
# elif media < 3:
#     print("Reprovado")
# elif media >= 3 and media < 6:
#     print("Exame")

class Provas():
    def __init__(self, n1: float, n2: float):
        self.n1 = n1
        self.n2 = n2

    def media(self):
        return (self.n1 + self.n2) / 2

    def resultado(self):
        if self.media() >= 6:
            return "Aprovado"
        elif self.media() < 3:
            return "Reprovado"
        elif self.media() >= 3 and self.media() < 6:
            return "Exame"

    def verificar_erro(self):
        if not isinstance(self.n1, (int, float)) or not isinstance(self.n2, (int, float)):
            return "Erro: As notas devem ser números."
        if self.n1 < 0 or self.n2 < 0:
            return "Erro: As notas não podem ser negativas."
        return None

    def __str__(self):
        erro = self.verificar_erro()
        if erro:
            return erro
        else:
            return f"Média: {self.media()}, Resultado: {self.resultado()}"

# teste
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

aluno = Provas(nota1, nota2)
print(aluno)


