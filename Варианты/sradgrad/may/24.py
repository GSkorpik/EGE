f=open('24.txt').readline()
#f='FFFFFFFFFFFFFFFF3FGGAGAGA2AA1UUUUUUUU1EEEEDDDD1'


s='BCDFGHJKLMNPQRSTVWXZ'
g='AEIOUY'
m=0
#print(f)
for a in range(1,10,2):

    ff=f.split(str(a))
    n = len(ff[0])

    if len(ff)>3:
        for i in range(1,len(ff)-1):
            f1=ff[i]
            gc=0
            sc=0
            for x in s:
                sc+=f1.count(x)
            for x in g:
                gc+=f1.count(x)
            #print(sc,gc)
            if sc==gc and (str(x) not in f1 for x in '1234567890') :
                if m<=len(f1)+2:
                    n1=n
                    m=len(f1)+2
            n+=len(f1)+2

print(n1)
