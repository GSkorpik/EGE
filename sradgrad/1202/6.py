from turtle import*
k=2
screensize(10000,10000)
speed(5)
left(90)

for i in range(2):
    for ii in range(2):
        forward(180*k)
        right(120)
    right(120)
right(150)
forward(15*k)
right(90)
forward(360*k)
right(90)
forward(15*k)
right(30)
forward(74)
up()
exitonclick()
print(180+180+180+180+30+360)