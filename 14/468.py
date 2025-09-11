zmax=0
for x in range(0,57):
    for y in range(0,57):
        a=5*57**7+3*57**6+x*57**5+6*57**4+6*57**3+y*57**2+3*57+5
        if a%56==0:
            z=y*57+x
            if (int(z**0.5)**2)==z:
                if z>zmax:
                    zmax=z
                    z2=x*57+y
print(z2)