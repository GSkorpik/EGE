from itertools import*
k=0
so='КМТ'
g='ОЕА'
for i in permutations("КОМЕТА"):
    s=''.join(i)
    if (s[0] in so) and (s[1] in g) and (s[2] in so) and (s[3] in g) and (s[4] in so) and (s[5] in g):
        k+=1
    if (s[0] in g) and (s[1] in so) and (s[2] in g) and (s[3] in so) and (s[4] in g) and (s[5] in so):
        k+=1
print(k)

'''
108)Петя составляет 6-буквенные слова из букв К, О, М, Е, Т, А.
Каждую букву нужно использовать ровно 1 раз, при этом нельзя ставить подряд две гласные или две согласные.
Сколько различных кодов может составить Петя?
'''