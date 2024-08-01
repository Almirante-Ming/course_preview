t = [[1,2],[3],[4,5,6],[7,7,7],[,10]] # ser dinamico 
# while n != 0:
#     n=int(input())
#     n=t.append
# lista com indices somados/planificacao da lista
count=0
i=0
vi=[]
while count < len(t):
    vi+=(t[i])
    # print(vi)
    i+=1
    count+=1

#soma dos valores contidos nos indices.
ns=sum(vi)  
print("a soma dos valores contidos na lista e", ns)