


f=open('24-223.txt').readline()
while 'CACAC' in f:
    f=f.replace('CACAC','CAC CAC')
    
#f='BABABCACABCB'
f=f.replace('CAC','***').replace('AB','**')

s='*'
while s in f:
    s+='*'

print(len(s)-1)
#CACACAB

'''
(Е. Джобс) Текстовый файл 24-223.txt содержит строку из символов A, B и C, всего не более чем 106 символов. 
Найдите максимальную длину строки, состоящей только из комбинаций AB и СAС. 
Например, в строке BABABCACABCB такая подстрока ABABCACAB (длина 9).
'''