for a in range(1,100):
    c=0
    for x in range(1,100):
        if (((not(5<=x<=54)) and (50<=x<=93))<=(x>a))==0:
            c+=1
    if c==20:
        print(a)
        break