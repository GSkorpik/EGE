def f( x, a1, a2 ):
  P = 155 <= x <= 177
  Q = 111 <= x <= 160
  A = a1 <= x <= a2
  return ((P<=(( not(Q) and not(A)) <= (not(P)))))

points = [ x+dx for x in [155,177,111,160]
                for dx in [-0.1, 0, 0.1] ]

#minLen = float('inf')
minLen=10**10

for a1 in points:
  for a2 in points:
    if all( f(x,a1,a2) for x in points ):
       minLen = min( minLen, round(a2-a1) )

print( minLen )

