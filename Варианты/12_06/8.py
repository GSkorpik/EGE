from  itertools import*


k=0
for i in product('АВСТРИЯ',repeat=7):
    s=''.join(i)
    if s.count('В')<=3 and (s.count('А')+s.count('Я')+s.count('И'))%2==0 and (s.count('А')+s.count('Я')+s.count('И'))!=0:
        k+=1

print(k)