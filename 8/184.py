from itertools import*
k=0
a='0123456789abcdef'
a2='02468ace'
a1='13579bdf'
for i in product(a,repeat=12):
    s=''.join(i)
    f=1
    for ii in range(len(s)-1):
        if (s[ii]<=s[ii+1]):
            f=0
            break
    if f == 1:
        for ii in range(len(s) - 1):
            if ((s[ii] in a1 and s[ii+1] in a2) or (s[ii] in a2 and s [ii+1] in a1))==1:
                f=0
                break
    if f==1:
        k+=1

print(k)
'''
184)Сколько шестнадцатеричных кодов чисел длиной 12 можно составить, 
если известно, что цифры идут в порядке убывания, 
при этом четные и нечетные цифры чередуются?
'''