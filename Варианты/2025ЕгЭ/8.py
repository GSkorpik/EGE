from itertools import*
k=0
for i in product('ЕИОРТЯ',repeat=6):
    s=''.join(i)
    k+=1
    if k%2==1 and s[0] not in 'РТЯ' and s.count('И')>=2:
        print(k)