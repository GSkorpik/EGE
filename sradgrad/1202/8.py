from itertools import*
k=0
for i in product('АДЛОСФЦЩ',repeat=4):
    k+=1
    s=''.join(i)
    if k%2!=0 and s[0]!='А' and s[-1]!='А' and s.count('Л')>=3:
        print(k)
        break