# 2) Dados dois inteiros m e n, qual a soma dos inteiros entre o intervalo inclusivo de m e n? Exemplo, para m=2 e n=6, a soma dos números entre 2 e 6 inclusivos é soma=2+3+4+5+6=20.

m = int(input())
n = int(input())

if m > n:
    aux = m
    m = n
    n = aux

cont = m
soma = 0

while cont <= n:
    soma += cont
    cont += 1

print("soma:", soma)
