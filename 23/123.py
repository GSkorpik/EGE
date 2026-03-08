
def f(x,n,l):
    if l<=5:
        if x==n:
            return 1
    if x>n: return 0
    if l>5: return 0
    return f(x+1,n,l+1)+f(x*2,n,l+1)+f(x+(x%4),n,l+1)

k=0
for x in range(1,1000):
    ff=f(x,80,0)
    if ff>0:
        k+=1
print(k)