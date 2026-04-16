from itertools import*
k=0
for i in product('АЕЛПРЬ',repeat=5):
    k+=1
    s=''.join(i)
    if  k%2==0 and s[0]!='Ь' and s[0]!='Р' and s.count('Л')>=2:
        print(k)