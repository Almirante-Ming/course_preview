n1=int(input("digite um número inteiro: "))
n2=int(input("digite o segundo número inteiro: "))

quo= n2%n1
#a variavel quo está dividndo o segundo número pelo primeiro e guardando o resto da divisão
rst=(n1-quo)+n2
#rts está realizando a operação de subtrair o primeiro numero pelo resto da divisão do primeiro pelo segundo, e somando com o segundo

print("o primeiro multiplo de ",n1," maior que ",n2, "é: ",rst)