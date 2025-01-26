import sys
sys.setrecursionlimit(2500)
def F(n):
    if n==1:
        return 1
    if n>1:
        return 2*n*F(n-1)

print((F(2024) - 4 * F(2023)) // F(2022))
def F( n ):
  a = [0, 1]
  for i in range(2, n+1):
      a.append(2*i*a[i-1])
  return a[n]
print((F(2024) - 4 * F(2023)) // F(2022))