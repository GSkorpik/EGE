m={}

def F(n):
    if n in m:
        return m[n]
    if n==0:
        return 0
    if n>0 and n <3:
        return 1
    res= F(n-2)+F(n-1)
    m[n]=res
    return res
print(F(47))
