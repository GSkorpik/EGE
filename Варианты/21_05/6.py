from turtle import*
k=15
screensize(10000,10000)
tracer(0)
left(90)

for i in range(3):
    forward(32*k)
    right(90)
    forward(38*k)
    right(90)
up()

forward(25*k)
right(90)
forward(21*k)
left(90)

down()

for i in range(3):
    forward(29*k)
    right(90)
    forward(18*k)
    right(90)
up()

for x in range(-100,100):
    for y in range(-100,100):
        goto(x*k,y*k)
        dot(4,'red')
exitonclick()