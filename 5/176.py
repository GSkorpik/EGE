for n in range(1,200):
    s=bin(n)[2:]

    r=s[1:]
    r=r.replace('1','*')
    r=r.replace('0','1')
    r=r.replace('*','0')
    s1=s[0]+r
    f=int(s1,2)
    #if f+n <=123:
    print(n,f,f+n,s,s1)