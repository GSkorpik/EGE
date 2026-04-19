
m=0
f=open('24-181.txt').readline()
#f='YYY.ABCD.ADB.ABF.AFAS.AAAAA.AAAAA.YYYYYYYYYY.'
s=[x for x in f.split('Y')]
for i in s:
    l=len(i)
    t=0
    for g in range(l):
        if i[g]=='.':
            t+=1
        if t<=5:
            m = max(m, g+1)
        if t>5:
            break
print(m)
'''
Текстовый файл 24-181.txt содержит строку из заглавных латинских букв и точек, 
всего не более чем из 106 символов. 
Определите максимальное количество идущих подряд символов, 
среди которых нет букв Y, а количество точек не превышает 5.
'''