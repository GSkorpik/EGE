from turtle import*
k=30
screensize(10000,10000)
left(90)
tracer(0)


left(315)
for i in range(3):
    left(315)
    forward(10*k)
    left(315)
left(45)
forward(15*k)
left(270)
forward(25*k)
left(270)
for i in range(2):
    forward(15*k)
    left(270)
up()

for x in range(-100,100):
    for y in range(-100,100):
        goto(x*k,y*k)
        dot(4,'red')

exitonclick()