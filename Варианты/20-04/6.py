from turtle import*
screensize(10000,10000)
tracer(0)
left(90)
k=30

for i in range(4):
    for n in range(10):
        forward(k)
        right(90)
        forward(k)
        left(90)
    right(90)
up()

for x in range(-2000,2000):
    for y in range(-2000,2000):
        goto(x*k,y*k)
        dot(4,'red')
exitonclick()
