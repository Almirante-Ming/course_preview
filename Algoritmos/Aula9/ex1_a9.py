aprovados = 0
reprovados = 0
contador = 0

while contador < 10:
    nome = input("Digite o nome do estudante: ")
    resultado = input("Digite o resultado do estudante ('a' para aprovado ou 'r' para reprovado): ")
    
    if resultado == "a":
        aprovados = aprovados + 1
    else:
        reprovados = reprovados + 1
 
    contador = contador + 1
 
print("Quantidade de estudantes aprovados:", aprovados)
print("Quantidade de estudantes reprovados:", reprovados)
 
if aprovados > 8:
    print("Bônus ao instrutor!")