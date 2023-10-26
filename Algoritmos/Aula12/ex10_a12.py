orig=int(input("insert a number: "))
inv=0
while orig!=0:
    resto=orig%10
    inv=inv*10+resto
    orig=orig//10
print("o inverso do número é: ",inv)