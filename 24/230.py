import string
from  fnmatch import*

f=open('24-230.txt').readline()

alf=string.ascii_uppercase
f=f.replace('ZZ','*')
for c in range(len(alf)):
    f=f.replace(alf[c],' ')

f=f.split('*')


m=0
for i in f:
    if fnmatch(i,'8???54???22') and ' ' not in i:
        print(i)
        m=max(m,int(i))

s=1
print(m)
for i in str(m):
    if int(i)%2!=0:
        s*=int(i)
print(s)
'''
(П. Финкель) Текстовый файл 24-230.txt состоит не более чем из 106 символов и содержит буквы английского алфавита и цифры.
 Определите максимальное число в этом файле, ограниченное двумя парами символов ZZ и удовлетворяющее маске «8???54???22», где символ ? обозначает любую цифру. 
Пример такого числа: 81235412322. Найдите произведение нечётных цифр найденного числа. 
'''