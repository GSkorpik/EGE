from itertools import*
k=0
so='ПЛСН'
p=[p1 +'Ь'+p2 for p1 in so for p2 in so if p1!=p2]
for i in permutations('АПЕЛЬСИН',7):
    s=''.join(i)
    f=1
    if 'Ь' in s:
        for ii in p:
            if ii in s:
                f=0
                break
    else:
        k+=1
    if f==0:
        k+=1
print(k)

'''
209)	(А. Куканова) Ася составляет 7-буквенные слова из букв А, П, Е, Л, Ь, С, И, Н. Все буквы слова различны. 
Буква Ь, если встречается, стоит между двумя согласными. 
Сколько таких слов может составить Ася?
'''