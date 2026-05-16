k=0
for n in range(4096,65536):
    h=hex(n)[2:]
    f=1
    if h.count('d')==1:
        for i in '13579bdf':
            if i+'d' in h or 'd'+i in h:
                f=0

        if f==1:
            k+=1

print(k)





#print(int('1000',16),int('10000',16))