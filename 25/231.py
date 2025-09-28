def pr(n):
    for i in range(2,round(n**0.5)+1):
        if n%i==0:
            return False
    if n>1:
        return True
def d(n):
    a=set()
    for i in range(2,round(n**0.5)):
        if n%i==0:
            if pr(i)==True:
                a.add(i)
            if pr(n//2)==True:
                a.add(n//i)
    if len(a)%2==1:
        return len(a)
    else:
        return False
def f(n):
    k=0
    for i in range(1,n+1):
        if pr(i)==True:
            k+=1
    if k%2==1:
        return k
    else:
        return False

for n in range(22,2023):
    if f(n)!=False and sum(map(int,str(n)))%22==0:
        print(n,f(n))



'''
231)На отрезке [22; 2022] найдите пять наибольших натуральных чисел с суммой цифр, кратной числу 22,
 факториал каждого из которых имеет нечетное количество простых делителей. 
Выведите найденные числа в порядке убывания, справа от каждого числа – количество простых делителей его факториала.
'''