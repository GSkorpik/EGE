from itertools import*
c='24680'
k=0

nc='13579'
for i in permutations('0123456789',5):
    s=''.join(i)
    flag=1
    for ii in range(len(s)-1):
        if (s[ii] in c and s[ii+1] in c) or (s[ii] in nc and s[ii+1] in nc):
            flag=0

    if s[0]!=0 and flag==1 and s[-1] in '05':
        k+=1
print(k)


'''
156)	Сколько существует чисел, делящихся на 5, десятичная запись которых содержит 5 цифр, 
причём все цифры различны и никакие две чётные и две нечётные цифры не стоят рядом.
'''