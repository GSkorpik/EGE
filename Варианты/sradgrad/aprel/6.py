from turtle import*
screensize(10000,10000)
tracer(0)
k=30
left(90)

for i in range(2):
    forward(8*k)
    left(270)
    backward(6*k)
    right(90)
up()

forward(5*k)
right(90)
backward(3*k)
left(90)
down()

for i in range(2):
    forward(7*k)
    right(90)
    backward(2*k)
    right(90)
up()

forward(3*k)
right(180)
backward(1*k)
down()

for i in range(2):
    forward(5*k)
    right(90)
    backward(5*k)
    right(90)
up()

for x in range(-100,100):
    for y in range(-100,100):
        goto(x*k,y*k)
        dot(4,'red')
exitonclick()

