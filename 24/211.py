k=0
m=0
f=open('24-211.txt').readline()
#f='BDEABECAFBDACBD'
for g in range(4):
    k=0
    for i in range(g,len(f)-3,3):
        if f[i:i+4] in ['ABEC', 'BDAC', 'CAFB', 'CFBA']:
            k+=1
            m=max(m,k)
        else:
            k=0


print(m)

'''
Текстовый файл 24-211.txt содержит строку из набора A, B, C, D, E, F, всего не более чем из 106 символов. 
Найдите максимальное количество подряд идущих четвёрок символов ABEC, BDAC, CAFB, CFBA, 
стоящих одна за другой и пересекающихся с соседними четвёрками одной буквой. 
Например, в строке BDEABECAFBDACBD такие пары составляют подстроку ABECAFBDAC = ABEC + СAFB + ВDAC, итого 3 четвёрки.
'''