def F(x, y, z, w):
    l1=w or y
    l2=x== l1
    l3= w<=z
    l4=y<=w
    l5=l4 and l3
    return int(l2 or l5)

print('x y z w | F(x, y, z, w)')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if F(x, y, z, w) == 0:
                    print(x, y, z, w, '|', F(x, y, z, w))