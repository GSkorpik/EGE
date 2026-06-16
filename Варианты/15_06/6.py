from turtle import*
k=30
left(90)
tracer(0)
screensize(10000,10000)


for i in range(2):
    forward(11*k)
    left(270)
    backward(11*k)
    right(90)
up()
forward(5*k)
right(90)
backward(3*k)
left(90)
down()
for i in range(2):
    forward(8*k)
    right(90)
    backward(12*k)
    right(90)
up()
forward(3*k)
right(180)
backward(6*k)
down()
for i in range(2):
    forward(9*k)
    right(90)
    backward(7*k)
    right(90)
up()
for x in range(-20,20):
    for y in range(-20,20):
        goto(x*k,y*k)
        dot(4,'red')

exitonclick()