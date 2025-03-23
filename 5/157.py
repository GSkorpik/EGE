for n in range(1,100):
    s=bin(n)[2:]
    while len(s)<8:
        s='0'+s
        '''
    s=s.replace('1','*')
    s=s.replace('0','1')
    s=s.replace('*','0')
    '''
    s1=''
    for c in s:
        if c=='0':
            s1+='1'
        else:
            s1+='0'
    r=int(s1,2)
    f=r-n
    if f==113:
        print(n)
        break