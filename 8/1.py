from itertools import *
k=0
for i in product('АОУ',repeat=5):
    k+=1
    if k==101:
        print(i)
        break


'''
k=0
for a in 'АОУ':
    for b in 'АОУ':
        for c in 'АОУ':
            for d in 'АОУ':
                for e in 'АОУ':
                    k+=1
                    if k==101:
                        print(a,b,c,d,e)
'''


