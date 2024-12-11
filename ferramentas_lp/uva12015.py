count=int(input())
for c in range(1, count+1):
    paginas={}
    
    for i in range(10):
        linha = input() .strip()
        url, relevancia=linha.rsplit(' ', 1)
        rev=int(relevancia)
        
        if rev not in paginas:
            paginas[rev]=[]
        paginas[rev].append(url)        
        
    sorte = max(paginas.keys())
    print(f'Case #{c}:')
    for url in paginas[sorte]:
        print(url)