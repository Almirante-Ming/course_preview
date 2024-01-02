# Inicialize as variáveis para contar os aprovados e reprovados
aprovados = 0
reprovados = 0

# Inicialize a variável para contar o número de estudantes
contador = 0

# Use um loop while para ler os resultados de cada estudante
while contador < 10:
    nome = input("Digite o nome do estudante: ")
    resultado = input("Digite o resultado do estudante ('a' para aprovado ou 'r' para reprovado): ")

    # Verifique o resultado e atualize as contagens
    if resultado == "a":
        aprovados = aprovados + 1
    else:
        reprovados = reprovados + 1

    contador = contador + 1

# Escreve a quantidade de estudantes aprovados e reprovados
print("Quantidade de estudantes aprovados:", aprovados)
print("Quantidade de estudantes reprovados:", reprovados)

# Verifique se mais de oito estudantes foram aprovados
if aprovados > 8:
    print("Bônus ao instrutor!")
