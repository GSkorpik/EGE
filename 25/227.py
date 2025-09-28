def pr(n):
    for i in range(2,round(n**0.5)+1):
        if n%i==0:
            return False
    if n>1:
        return True
def d(n):
    for i in range(2,round(n**0.5)):
        if n%i==0:
            if pr(i)==True and i>10:
                return i
                break
            elif pr(n//i)==True and i>10:
                return n//i
                break
            break
    return False
for n in range(200,2022):
    if d(n)!=False:
        print(n,d(n))

'''
227)На отрезке [200; 2022] найдите пять наибольших составных натуральных чисел, минимальный простой делитель которых больше числа 10.
Выведите найденные числа в порядке убывания, справа от каждого числа – его минимальный простой делитель.
'''