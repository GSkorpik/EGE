from turtle import*
tracer(0)
k=30
left(90)
screensize(10000,10000)

for i in range(2):
    forward(10*k)
    right(90)
    forward(18*k)
    right(90)
up()
forward(5*k)
right(90)
forward(7*k)
left(90)

down()
for i in range(2):
    forward(10*k)
    right(90)
    forward(7*k)
    right(90)
up()

for x in range(-50,50):
    for y in range(-50,50):
        goto(k*x,y*k)
        dot(4,'red')

exitonclick()
