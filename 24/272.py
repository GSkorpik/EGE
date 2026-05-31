import string

f=open('24-264.txt').readline()
alf=string.ascii_uppercase
dec='123456789'
for i in alf:
    f=f.replace(i,'A')
for i in dec:
    f=f.replace(i,'0')
#print(f)
s='0'
while s in f:
    s+='A0'


if s[:-1] in f:
    print(len(s)-1)
else:
    print(len(s) - 2)

s='A'
while s in f:
    s+='0A'
if s[:-1] in f:
    print(len(s)-1)
else:
    print(len(s) - 2)

'''
(ЕГЭ-2023) Текстовый файл 24-264.txt состоит не более чем из 106 символов и содержит только заглавные буквы латинского алфавита и цифры. 
Определите максимальную длину подстроки, в которой ни ода буква не стоит рядом с буквой и ни одна цифра не стоит рядом с цифрой.
'''