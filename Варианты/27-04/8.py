from itertools import*

a=set()
for i in permutations('ТРАТАТА'):
    a.add(i)

print(len(a))


