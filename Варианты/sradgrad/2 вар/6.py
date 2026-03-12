from turtle import*
k=20
screensize(10000,10000)
tracer(0)
left(90)

for i in range(7):
    forward(17*k)
    right(90)
    forward(26*k)
    right(90)
up()
forward(4*k)
right(90)
forward(6*k)
left(90)
down()
for i in range(7):
    forward(278*k)
    right(90)
    forward(345*k)
    right(90)
up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*k,y*k)
        dot(4,'red')
print(279*346+27*4+14*6)
exitonclick()
