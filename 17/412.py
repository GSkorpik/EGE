'''def d(a1,a2):
    a=set()


    if a1<a2:
        for i in range(1, round(a1 ** 0.5) + 1):
            if a1%i==0 and a2%i==0:
                a.add(i)
                if a1%(a1//i)==0 and a2%(a1//i)==0:
                    a.add(a1//i)
    else:
        for i in range(1, round(a2 ** 0.5) + 1):
            if a1%i==0 and a2%i==0:
                a.add(i)
                if a1%(a2//i)==0 and a2%(a2//i)==0:
                        a.add(a2//i)

    if len(a)>0:
        return  max(a)
    else: return False
'''
def f(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a

k=0
maxx=0
a=[int(x) for x in open('17-411.txt')]
a3=[x for x in a if x%10==3]
for i in range(len(a)-1):
    x=f(a[i],a[i+1])
    if min(a3)%x==0:
        k+=1
        maxx=max(maxx,a[i]+a[i+1])

print(k,maxx)

'''
412)	(К. Багдасарян) В файле 17-411.txt содержится последовательность натуральных чисел, не превышающих 10000.
Определите количество пар последовательности,
для которых минимальный элемент последовательности, оканчивающийся на 3,
кратен наибольшему общему делителю пары.
В ответе запишите количество найденных пар, 
затем максимальную из сумм элементов таких пар.
В данной задаче под парой подразумевается два идущих подряд элемента последовательности.
'''