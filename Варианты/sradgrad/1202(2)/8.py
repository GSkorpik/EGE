from itertools import*
k=0
for i in product('ВЕЖХЧШЭЮ',repeat=4):
    k+=1
    s=''.join(i)
    if k%2!=0 and s[0]!='В' and s[-1]!='В' and s.count('Ч')>=3:
        print(k)
        break