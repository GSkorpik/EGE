from turtle import*
k=40
screensize(10000,10000)
speed(10)

for i in range(2):
    p=pos()
    goto(p+(3*k,k*4))
    p = pos()
    goto(p + (-3 * k, k * 4))
    p = pos()
    goto(p + (-3 * k, k * -4))
    p = pos()
    goto(p + (3 * k, k * -4))
up()
for x in range(-5,5):
    for y in range(0,10):
        goto(x*k,y*k)
        dot(4,'red')

exitonclick()