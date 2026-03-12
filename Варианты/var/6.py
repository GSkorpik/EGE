from turtle import*
screensize(10000,10000)
tracer(0)
k=30
left(90)

for i in range(2):
    forward(3*k)
    left(90)
    backward(10*k)
    left(90)
up()
backward(10*k)
right(90)
forward(8*k)
left(90)
down()
for i in range(2):
    forward(16*k)
    right(90)
    forward(8*k)
    right(90)
up()
for x in range(-10,50):
    for y in range(-10,50):
        goto(x*k,y*k)
        dot(4,'red')

exitonclick()