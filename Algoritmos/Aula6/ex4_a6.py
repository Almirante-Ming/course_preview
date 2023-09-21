n1=int(input("digite o tempo em segundos: "))

tS=n1%60

tM=(n1//60)%60
tH=(n1//60)//60

print("seu tempo convertido em: ",tH,"H",tM,"M",tS,"SS")