from turtle import*
k=40
screensize(10000,10000)
speed(10)

for i in range(3):
    p=pos()
    goto(p+(3*k,k*2))
    p = pos()
    goto(p + (-2 * k, k * 3))
    p = pos()
    goto(p + (-3 * k, k * -2))
    p = pos()
    goto(p + (2 * k, k * -3))
up()
for x in range(-5,5):
    for y in range(0,10):
        goto(x*k,y*k)
        dot(4,'red')

exitonclick()


'''
Повтори 3 раз 
  Сместиться на (3, 2) 
  Сместиться на (-2, 3) 
  Сместиться на (-3, -2) 
  Сместиться на (2, -3)
конец
Найдите площадь полученной фигуры.
'''