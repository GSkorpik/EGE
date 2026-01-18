for a in range(1,100):
    k=0
    for x in range(1,1000):
        for y in range(1,1000):
            if ((12*x+2*y>56) or (x>2*y) or (5*x+y<a))==0:
                print(a)
                break

#не совпадает с ответом