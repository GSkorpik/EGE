def f(x,y,a):
    if y==7:
        a.add(x)
        return len(a)

    return f(x+7,y+1,a), f(x+6,y+1,a), f(x-5,y+1,a)




a=set()
print(f(10,0,a))