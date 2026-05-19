from itertools import*

k=0
for i in product('АЕЛРСТ', repeat=5):
    k+=1
    s=''.join(i)
    if s[0] not in 'АСТ' and s.count('Л')==2 and 'ЛЛ' not in s and k%2==0:
        print(k)