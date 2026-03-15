from fnmatch import*

for i in range(1230056,10**8):
    if fnmatch(str(i),'1*23??56')==1 and i%171==0:
        print(i,i//171)
