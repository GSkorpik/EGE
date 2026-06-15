from turtle import*
k=30
left(90)
screensize(10000,10000)
speed(5)

for i in range(2):
    down()
    for ii in range(2):
        forward(10*k)
        right(90)
        forward(10*k)
        right(90)
    up()
    forward(8*k)
    left(270)
    forward(8*k)
    left(90)

right(180)
forward(6*k)
down()
for i in range(4):
    forward(10*k)
    right(270)

for x in range(-50,50):
    for y in range(-50,50):
        goto(x*k,y*k)
        dot(4,'red')

exitonclick()
