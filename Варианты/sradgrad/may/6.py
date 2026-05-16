from turtle import*
k=15
speed(10)
screensize(10000,10000)


for i in range(8):
    forward(95*k)
    right(135)
    forward(83*k)
    right(45)
tracer(0)
up()

for x in range(-100,100):
    for y in range(-100,100):
        goto(x*k,y*k)
        dot(4,'red')
exitonclick()