##Contando de 1 a 100 em incrementos de 1
for i in range(1, 101): print(i) 

j=1
while j <= 100:
    print(j)
    j+=1

##Contando de 100 a 1 em decrementos de 1
for i in range(100, 0, -1): print(i)

j=100
while j >= 1:
    print(j)
    j-=1
    
##Contando de 7 a 77 em incrementos de 7
for i in range(7, 78, 7): print(i)

j=7
while j <= 78 :
    print(j)
    j+=7
    
##Contando de 20 a 2 em decrementos de 2
for i in range(20, 1, -2): print(i)

j=20
while j >= 1:
    print(j)
    j-=2

##Incrementando entre os valores 2, 5, 8, 11, 14, 17, 20
for i in range(2, 21, 3): print(i)

j=2
while j <= 21 :
    print(j)
    j+=3
    
##Decrementando entre os valores 99, 88, 77, 66, 55, 44, 33, 22, 11, 0:
for i in range(99, -1, -11): print(i)

j=99
while j > -1:
    print(j)
    j-= 11