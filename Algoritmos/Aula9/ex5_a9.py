num= int(input("digite um número: "))
n=1
tri=n*(n+1)*(n+2)

while tri < num:
    n+=1
    tri=n*(n+1)*(n+2)
if tri ==num:
    print(f"{num} é triangular")
    print(f"{n}*{n+1}*{n+2}")
else:
    print(f"{num} não é triangular")