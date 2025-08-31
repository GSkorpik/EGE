def func(x):
    a, b = 0, 1
    for i in range(x):
        print(a, end=' ')
        a, b = b, a + b
x=int(input())
print(func(x))