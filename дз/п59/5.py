def men(x):
    o = oct(x)[2:]

    if int(o)<8**10:

        o = o.zfill(10)
    print(o)

x=int(input())
men(x)
