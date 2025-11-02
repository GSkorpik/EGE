'''

def f(n):

    if n<5: return 1+2*n
    if n>=5 and n%3==0:
        return 2*(n+1)*f(n-2)
    else:
        return 2*n+1+f(n-1)+f(n-2)
'''

def f(n):
    a=[1,3]
    for i in range(2,n+1):
        if i<5:
            a.append(1+2*i)
        elif  i%3==0:
            a.append(2*(i+1)*a[i-2])
        else:#  i%3!=0 :
            a.append(2*i+1+a[i-1]+2*a[i-2])

    return a[n]

print(f(15))

'''
16)	Алгоритм вычисления функции F(n) задан следующими соотношениями:
		F(n) = 1+2n при n < 5
		F(n) = 2·(n + 1)·F(n–2), если n ≥ 5 и делится на 3,
		F(n) = 2·n + 1 + F(n–1) + 2·F(n–2), если n ≥ 5 и не делится на 3.
Чему равно значение функции F(15)?

'''