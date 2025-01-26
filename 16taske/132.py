#           F(3516)=(2*3516-1)*F(3515)
#           F(3515)=(2*3515-1)*F(3514)
#           F(3514)=(2*3514-1)*F(3513)


print((2*3516-1)*(2*3515-1)*(2*3514-1))

def F( n ):
  a = [0, 1]
  for i in range(2, n+1):
      a.append((2*i -1)*a[i-1])
  return a[n]
print(F(3516)//F(3513))