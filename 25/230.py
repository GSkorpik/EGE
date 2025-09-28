def pr(n):
    for i in range(2,round(n**0.5)+1):
        if n%i==0:
            return False
    if n>1:
        return True
def d(n):
    a=set()
    for i in range(2,n+1):
        if n%i==0:
            if pr(i)==True:
                a.add(i)
    if len(a)%2==1:
        return len(a)
    else:
        return False
def f(n):
    a=1
    for i in range(1,n+1):
        a*=i
    return a

for n in range(2,14):
    a=f(n)
    if d(a)!=False:
        print(n,d(a))

'''
230) На отрезке [2; 14] найдите пять наибольших натуральных чисел, факториал каждого из которых имеет нечетное количество простых делителей.
 Выведите найденные числа в порядке убывания, справа от каждого числа – количество простых делителей его факториала.
'''
