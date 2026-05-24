from  itertools import*
k=0
for i in product('АКОРСТ', repeat=5):
    k+=1
    s=''.join(i)
    if s[0] not in 'АСТ' and s.count('О')==2 and k%2==0:
        print(s,k)

