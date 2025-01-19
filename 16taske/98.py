def F(n):
    if n==0:
        return 0
    if n>0 and n%2==0:
        return F(n//2)+3
    if n>0 and n%2==1:
        return 2*F(n-1)+1

#множество чисел
a=set()
for i in range(1,1000):
    a.add(F(i))#добавить элемент в множество
print(len(a))#колл-во элементов