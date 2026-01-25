from itertools import*
k=0
for i in permutations('ВОРОТА'):
    s=''.join(i)
    a=1
    for ii in product('ОА',repeat=2):
        ss=''.join(ii)
        if s.count(ss)!=0:
            a*=0
    if a==1:
        print(s)
        k+=1
print(k//2)



'''
134)Артур составляет 6-буквенные коды перестановкой букв слова ВОРОТА. 
При этом нельзя ставить рядом две гласные. 
Сколько различных кодов может составить Артур?
'''