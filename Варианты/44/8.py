from itertools import*
k=0
for s in product('АПРСУ',repeat=5):
    k+=1
    s=''.join(s)
    if k==2527: print(s)
    if s[0]=='У' and 'АА' not in s:
        print(k,s)
        break