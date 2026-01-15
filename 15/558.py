for a in range(500,0,-1):
    for x in range(0,100):
        for y in range(0,100):
            if ((5*x+y>63)or (x>2*y)or (3*x+2*y)<a)==0:
                print(a)
                break

