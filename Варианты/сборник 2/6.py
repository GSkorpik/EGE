from turtle import*
left(90)
tracer(0)
k=30
screensize(10000,10000)

for i in range(4):
    forward(19*k)
    left(180)
    backward(10*k)
    right(90)
up()
backward(5*k)
left(90)
forward(4*k)
right(90)
down()

for i in range(2):
    forward(15*k)
    left(90)
    forward(8*k)
    left(90)

up()
for x in range(-30,20):
    for y in range(-20,50):
        goto(x*k,y*k)
        dot(4,'red')


exitonclick()