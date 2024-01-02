# 1) Dada uma sequência de números, seguida pelo zero, qual o maior número da sequência?

# primeiro número da sequênia
n = int(input())

# maior número até o momento
maior = n

# verifica se chegou no fim da sequência
while n != 0:
    if n > maior:
        # atualiza o maior número até o momento
        maior = n
    # próximo número da sequência
    n = int(input())

print("maior", maior)
