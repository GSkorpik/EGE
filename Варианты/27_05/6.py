from turtle import*
tracer(0)
left(90)
k=20
screensize(10000,10000)

for i in range(9):
    forward(27*k)
    right(90)
    forward(30*k)
    right(90)
up()

forward(1*k)
right(90)
forward(4*k)
left(90)

down()
for i in range(9):
    forward(166*k)
    right(90)
    forward(177*k)
    right(90)
up()
for x in range(-50,50):
    for y in range(-100,100):
        goto(x*k,y*k)
        dot(4,'red')
exitonclick()