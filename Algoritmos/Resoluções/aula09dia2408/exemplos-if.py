salario = float(input("informe teu salario: "))
nota = float(input("informe tua nota: "))
numero = int(input("informe teu numero da sorte: "))
idade = int(input("informe tua idade: "))

print("\nvoce ganha", salario)
if salario > 5000:
    print("vc ta bem ein!")

print("\nvoce tirou nota", nota)
if nota < 7:
    print("vc esta de recuperacao!")

print("\nteu numero da sorte eh", numero)
if numero % 2 == 0:
    print("numero par")
if numero % 5 == 0:
    print("numero multiplo de 5.")

print("\ntua idade eh", idade)
if idade >= 18:
    # Obrigatório usar indentação para indicar o bloco
    print("vc eh maior de idade,")
    print("ja eh responsavel legalmente.")

print("\nfim do programa.")
