from turtle import*
screensize(10000,10000)
left(90)
tracer(0)
k=70

left(15)
for i in range(7):
    left(30)
    forward(10*k)
    left(60)
up()

for x in range(-50,50):
    for y in range(-50,50):
        goto(k*x,y*k)
        dot(4,'red')

exitonclick()