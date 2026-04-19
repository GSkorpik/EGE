from turtle import*
screensize(10000,10000)
tracer(0)
k=30
left(90)

for i in range(2):
    forward(3*k)
    right(90)
    forward(20*k)
    right(90)
up()
backward(8*k)
right(90)
forward(9*k)
left(90)
down()
for i in range(2):
    forward(16 * k)
    right(90)
    forward(8 * k)
    right(90)
up()
for x in range(-100,100):
    for y in range(-100,100):
        goto(x*k,y*k)
        dot(4,'red')

exitonclick()
