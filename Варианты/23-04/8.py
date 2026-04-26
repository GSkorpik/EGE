from itertools import*
k=0
for s in product('АВДПР',repeat=4):
    k+=1
    s=''.join(s)
    if s =='ВДПР':
        print(k)
        break