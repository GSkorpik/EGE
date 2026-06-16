

n=0
b=[]
for l in open('9.txt'):
    n+=1
    a=[int(x) for x in l.split()]
    if int(sum(a)**0.5) in a and any(str(x)[0]==str(x)[-1] for x in a):
        b.append(n)

print(max(b)+min(b))