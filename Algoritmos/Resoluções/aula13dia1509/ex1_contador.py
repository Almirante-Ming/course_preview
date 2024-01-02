# Inicialize as variáveis
total = 0
contador = 1

# Use um loop para ler as notas dos cinco estudantes
while contador <= 5:
    nota = float(input(f"Digite a nota do {contador}º estudante (entre 0 e 10): "))
    total = total + nota
    contador = contador + 1

# Calcule a média
media = total / 5

# Escreve a média da classe
print("A média da classe é:", media)
