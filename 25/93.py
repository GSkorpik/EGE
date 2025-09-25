def d(n):
    n=str(n)
    for i in n:
        if int(i)%2==0:
            return False
    return True

summ=0
for n in range(1686,13276):
    if d(n)==True:
        summ+=sum(map(int,str(n)))

print(summ)





'''
93)	(К. Амеличев) Среди целых  чисел, принадлежащих числовому отрезку [1686; 13276], найдите числа, все цифры которых нечетные. 
Ответом будет сумма цифр найденных чисел.
'''