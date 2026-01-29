from itertools import*
k=0
for x in range(4,7):
    #c=[i for i in product('ЧОАНИМЕ',repeat=x) if i.count('М')==3]
    #k+=len(c)
    for i in product('ЧОАНИМЕ',repeat=x):
        s=''.join(i)
        if s.count('М')==3:
            k+=1
print(k)


'''
217)	(А. Куканова) Леся составляет слова, содержащие ровно 3 буквы М, из букв Ч, О, А, Н, И, М, Е.
Слово может иметь длину от 4 до 6 букв.
Сколько различных слов может составить Леся?
'''