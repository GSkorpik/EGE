for n in range(256):
    b=bin(n)[2:].zfill(8)
    r=b[:2]+b[-2:]
    r=int(r,2)
    if n>130 and r==10:
        print(n)