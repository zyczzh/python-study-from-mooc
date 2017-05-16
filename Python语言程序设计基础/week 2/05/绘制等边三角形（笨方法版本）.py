import turtle
def trangle():
    turtle.setup(1300,1300,0,0)
    pythonsize=10
    forward=50
    turtle.pensize(pythonsize)
    turtle.pencolor("red")#注意单词
    #笨方法，一步一笔
    turtle.seth(0)
    turtle.fd(forward)
    turtle.seth(120)
    turtle.fd(forward)
    turtle.seth(240)
    turtle.fd(forward)
trangle()
