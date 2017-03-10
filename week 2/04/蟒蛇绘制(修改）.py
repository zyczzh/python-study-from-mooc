import turtle
import random
def drawSnake(rad,angle,len,neckrad):
    setcolor=['A','B','C','D','E','F',1,2,3,4,5,6,7,8,9,0]
    for i in range(len):
        color=random.sample(setcolor,6)
        a="#"
        for j in color:
            a=a+str(j)
        turtle.pencolor(a)
        turtle.circle(rad,angle)
        turtle.circle(-rad,angle)
    turtle.circle(rad,angle/2)
    turtle.fd(rad)
    turtle.circle(neckrad+1,180)
    turtle.fd(rad*2/3)
def main():
    turtle.setup(1300,800,0,0)
    pythonsize=30
    turtle.pensize(pythonsize)
    turtle.seth(-40)#影响了蟒蛇的方向
    drawSnake(40,80,5,pythonsize/2)
main()
