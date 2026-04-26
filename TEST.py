



a1=125

b1=oct(a1)[2:]

max1=max(int(x) for x in str(b1))
i1=b1.index(str(max1))
print(i1,max1,b1)