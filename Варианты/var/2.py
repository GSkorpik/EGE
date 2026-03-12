
print('x y z w | f')
for x in 0,1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f=(not(z)and y and x and not(w))or(not(z)and y and not(x)and not(w))or(z and y and x and not(w))

                if f==1:
                    print(x,y,z,w,'|',f)
#wzxy