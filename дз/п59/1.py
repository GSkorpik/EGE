def func(x):
    x = str(x)
    for i in x[::-1]:
        print(i)

x = int(input())
func(x)