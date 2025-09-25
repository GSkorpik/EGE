def d(n):
    mini=0

    for c in str(n):
        if int(c)<mini:
            return False
        mini=int(c)
    return True
summ=0
for n in range(1395,22718):
    if d(n)==True:
        summ+=n

print(summ)






'''
95)	(К. Амеличев) Среди целых  чисел, принадлежащих числовому отрезку [1395; 22717], найдите числа, все цифры которых расположены в порядке неубывания. 
Ответом будет сумма найденных чисел.
'''