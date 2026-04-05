from turtle import*
screensize(10000,10000)
k=30
tracer(0)
left(90)


for i in range(2):
    forward(14*k)
    left(270)
    backward(12*k)
    right(90)
up()

forward(9*k)
right(90)
backward(7*k)
left(90)
down()
for i in range(2):
    forward(13*k)
    right(90)
    forward(6*k)
    right(90)
up()
forward(7*k)
right(180)
backward(2*k)
down()

for i in range(2):
    forward(10*k)
    right(90)
    forward(12*k)
    right(90)
up()

for x in range(-20,10):
    for y in range(-20,50):
        goto (x*k,y*k)
        dot(4,'red')

exitonclick()