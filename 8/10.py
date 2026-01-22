from itertools import*
k=0
p=product('АОУ',repeat=5)
for x in p:
    k+=1
    s=''.join(x)
    if s=='ОАОАО':
        print(k)
        break



'''
k=0
for a in 'АОУ':
    for b in 'АОУ':
        for c in 'АОУ':
            for d in 'АОУ':
                for e in 'АОУ':
                    k+=1
                    if a+b+c+d+e=='ОАОАО':
                        print(k)'''