def F(n):
    a=[0,1, 2]
    for i in range(3,n+1):
        a.append(i+a[i-2])
    return a[n]
print(F(2023)+F(2020))
