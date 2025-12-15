from turtle import*
screensize(800,800)
tracer(0)
k=40
left(90)
forward(9*k)

right(90)
for i in range(2):
    forward(3*k)
    right(90)
    forward(3*k)
    right(270)
for i in range(2):
    forward(3 * k)
    right(90)
forward(9*k)
up()

for x in range(-10,20):
    for y in range(-10,20):
        goto(x*k,y*k)
        dot(4,'red')
exitonclick()

'''
Вперёд 9 Направо 90 
Повтори 2 [Вперёд 3 Направо 90 Вперёд 3 Направо 270] 
Повтори 2 [Вперёд 3 Направо 90] 
Вперёд 9
Определите, сколько точек с целочисленными координатами будут находиться внутри области,
ограниченной линией, заданной данным алгоритмом. Точки на линии учитывать не следует.
'''