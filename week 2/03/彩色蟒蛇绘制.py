import turtle
def drawSnake(rad,angle,len,neckrad,):
    #rad:圆形轨迹半径的位置
    #angle：圆形爬行的弧度值
    #len：循环的次数
    #neckrad：返回半径的位置
    for i in range(len):
        turtle.circle(rad,angle)
        turtle.circle(-rad,angle)
    turtle.circle(rad,angle/2)
    turtle.fd(rad)
    turtle.circle(neckrad+1,180)
    turtle.fd(rad*2/3)
def main():
    turtle.setup(1300,800,0,0)
    pythonsize=10
    turtle.pensize(pythonsize)
    turtle.pencolor("red")
    turtle.seth(-40)
    drawSnake(10,80,5,pythonsize/2)
main()
