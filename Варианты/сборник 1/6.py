from turtle import*
left(90)
tracer(0)
k=30
screensize(10000,10000)

for i in range(4):
    forward(9*k)
    left(180)
    backward(10*k)
    right(90)
up()
backward(7*k)
left(90)
forward(3*k)
right(90)
down()

for i in range(2):
    forward(17*k)
    left(90)
    forward(20*k)
    left(90)

up()
for x in range(-30,20):
    for y in range(-20,20):
        goto(x*k,y*k)
        dot(4,'red')


exitonclick()