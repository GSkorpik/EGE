from turtle import*
screensize(10000,10000)
tracer(0)
k=30
left(90)

for i in range(2):
    forward(10*k)
    right(90)
    forward(20*k)
    right(90)
up()
backward(15*k)
right(90)
forward(8*k)
left(90)
down()
for i in range(2):
    forward(30*k)
    right(90)
    forward(40*k)
    right(90)
up()

for x in range(-100,100):
    for y in range(-100,100):
        goto(x*k,y*k)
        dot(4,'red')
exitonclick()



