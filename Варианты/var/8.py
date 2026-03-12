from itertools import*
a='ИРСТУЦ'
k=0
for i in product(a,repeat=5):
    k+=1
    s=''.join(i)
    if s.count('И')==2 and 'ЦЦ' not in s:
        print(k)
        