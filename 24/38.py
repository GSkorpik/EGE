
f=open('k7c-6.txt')
f=f.readline()
k=0
for i in range(len(f)-2):
    if len(set(f[i:i+3]))==3:
        k+=1
print(k)

'''k=0
for i in range(len(f)-2):
    if f[i]!=f[i+1] and f[i+1]!=f[i+2] and f[i]!=f[i+2] and f[i]!=f[i+2]:
        k+=1
print(k)
'''
'''
(А.М. Кабанов) В текстовом файле k7c-6.txt находится цепочка из символов латинского алфавита A, B, C, D, E, F.
Найдите количество цепочек длины 3, в которых символы не совпадают.
'''