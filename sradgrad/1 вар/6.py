from turtle import*
k=10
screensize(10000,10000)
tracer(0)
left(90)

for i in range(7):
    forward(15*k)
    right(90)
    forward(23*k)
    right(90)
up()
forward(3*k)
right(90)
forward(5*k)
left(90)
down()
for i in range(7):
    forward(252*k)
    right(90)
    forward(398*k)
    right(90)
up()

for x in range(0,30):
    for y in range(-1,100):
        goto(x*k,y*k)
        dot(4,'red')
exitonclick()
#137
print(253*399+137)