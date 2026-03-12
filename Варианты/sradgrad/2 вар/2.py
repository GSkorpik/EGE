print('x y z w | F')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f=(not(w)and z and not(y) and not(x)) or (not(w) and z and y and not(x)) or (not(w) and z and y and x)
                if f ==1:
                    print(x,y,z,w,f)