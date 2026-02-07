from itertools import*
k=0
p=product('АЕИКМСЧ',repeat=5)
for i in p:
    k+=1
    s=''.join(i)
    if s=='МАСИК':
        k1=k
    if s=='ЧЕЧИК':
        k2=k
print(k2-k1-1)