def f(n):
    alf='0123456789abcdefghij'
    s=''
    while n!=0:
        s=alf[n%20]+s
        n//=20
    return s
a=set()
for n in range(1,1000):
    s=f(n)
    l=len(s)
    if l%2==0:
        r=s[(l//2)-1:]+s[:l//2]
    else:
        r=s+'a'

    r=int(r,20)
    if r>190:
        a.add(n)

print(min(a))