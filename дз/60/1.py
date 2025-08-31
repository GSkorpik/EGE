def maxx(a,b,c):
    if a>=b and a>=c:
        m=a
    if b>=a and b>=c:
        m=b
    else:
        m=c
    return m

a=int(input())
b= int(input())
c=int(input())

print(maxx(a,b,c))