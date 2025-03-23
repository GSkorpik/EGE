for n in range(1000,10000):
    s=oct(n)[2:]
    s= s.replace('2','1')
    s = s.replace('4', '1')
    s = s.replace('0', '1')
    s = s.replace('6', '1')
    s=s+str(n%8)
    #print(s)
    n1=int(s,8)
    #print(n)
    s = oct(n1)[2:]
    #print(s)
    s = s.replace('2', '1')
    s = s.replace('4', '1')
    s = s.replace('0', '1')
    s = s.replace('6', '1')
    #print(s)
    s = s +str( n1 % 8)
    #print(s)
    r = int(s, 8)
    #print(r)
    if r%234==0:
        print(r)
