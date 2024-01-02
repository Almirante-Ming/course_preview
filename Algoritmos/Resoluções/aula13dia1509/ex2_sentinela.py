total = 0
contador = 0
nota = float(input("Digite a nota do estudante (ou -1 para encerrar): "))

while nota != -1:
    if 0 <= nota <= 10:
        total = total + nota
        contador = contador + 1
    else:
        print("A nota deve estar entre 0 e 10. Tente novamente.")

    nota = float(input("Digite a nota do estudante (ou -1 para encerrar): "))

if contador > 0:
    media = total / contador
    print("A média da classe é:", media)
else:
    print("Nenhuma nota válida foi inserida.")
