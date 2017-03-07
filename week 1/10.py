import turtle
import time
turtle.pensize(2)
turtle.bgcolor("black")#背景色设置
colors=["red","yellow",'purple','blue']#双引号和单引号的区别
turtle.tracer(False)
for x in range(400):
    turtle.forward(2*x)
    turtle.color(colors[x%4])
    turtle.left(91)
turtle.tracer(True)#True 要大写

