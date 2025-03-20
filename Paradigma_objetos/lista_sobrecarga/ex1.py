import math

class Fracao:
    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise ValueError("O denominador não pode ser zero")
        self.numerador = numerador
        self.denominador = denominador
        self.simplifica()

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    def simplifica(self):
        mdc = math.gcd(self.numerador, self.denominador)
        self.numerador //= mdc
        self.denominador //= mdc
        if self.denominador < 0:
            self.numerador *= -1
            self.denominador *= -1

    def __add__(self, outra):
        numerador = self.numerador * outra.denominador + outra.numerador * self.denominador
        denominador = self.denominador * outra.denominador
        resultado = Fracao(numerador, denominador)
        return resultado

    def __sub__(self, outra):
        numerador = self.numerador * outra.denominador - outra.numerador * self.denominador
        denominador = self.denominador * outra.denominador
        resultado = Fracao(numerador, denominador)
        return resultado

    def __mul__(self, outra):
        numerador = self.numerador * outra.numerador
        denominador = self.denominador * outra.denominador
        resultado = Fracao(numerador, denominador)
        return resultado

    def __truediv__(self, outra):
        if outra.numerador == 0:
            raise ZeroDivisionError("Não é possível dividir por uma fração com numerador 0")
        numerador = self.numerador * outra.denominador
        denominador = self.denominador * outra.numerador
        resultado = Fracao(numerador, denominador)
        return resultado


f1 = Fracao(4, 8)
f2 = Fracao(2, 3)

soma = f1 + f2
print(f"Soma: {soma}")
