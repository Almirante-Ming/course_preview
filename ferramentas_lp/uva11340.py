import re

n=int(input())
k=int(input())

char_cost={}


for _ in range(k):
    c=input()
    key, value = c.split()
    char_cost[key]=int(value)

m = int(input())

payment = 0.0

for _ in range(m):
    line_arc=input()
    article = re.findall('.', line_arc)
    for arc in article:
        if arc in char_cost:
            payment += char_cost[arc]
        else:
            payment += 0.0
 
print(f'{payment/100:.2f}'+'$')
