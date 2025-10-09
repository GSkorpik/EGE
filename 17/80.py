
def f(n):
    a0 =0
    a1 =0
    a2 =0
    a3 =0
    a4 =0
    a5 =0
    a6 =0
    a7 =0
    a8 = 0
    a9 = 0
    for r in str(n):
        a0 += r.count('0')
        a1 += r.count('1')
        a2 += r.count('2')
        a3 += r.count('3')
        a4 += r.count('4')
        a5 += r.count('5')
        a6 += r.count('6')
        a7 += r.count('7')
        a8 += r.count('8')
        a9 += r.count('9')

    if a0<=1 and a1<=1 and a2<=1 and a3<=1 and a4<=1 and a5<=1 and a6<=1 and a7<=1 and a8<=1 and a9<=1:
        return True
    else:
        return False

'''n=27
k=0
while n<900000:
    print(n)
    k+=1
    n=n*2

print(k)'''

k=0
for n in range(16):
    r = 27 * (2 ** n)
    if f(r)==True:
        k+=1
        maxx=r
print(k,maxx)




'''
80)	(Б.С. Михлин) Рассматривается множество целых чисел на интервале [27, 900 000], 
которые образуют геометрическую прогрессию со знаменателем 2: 27, 54, 108, ... 
Найдите среди них числа, у которых нет повторяющихся цифр. 
В ответе через пробел напишите сперва количество таких чисел, а затем максимальное из них.
'''