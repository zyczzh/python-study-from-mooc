import turtle
def trangle(forward,angle,len):#len是重复的次数
     for i in range(len):
        angle=angle+120#每次角度变换数
        turtle.fd(forward)
        turtle.seth(angle)
def main():
    turtle.setup(1300,1300,0,0)
    pythonsize=10
    forward=100
    angle=0#初始角度
    turtle.pensize(pythonsize)
    turtle.pencolor("red")#注意单词
    trangle(forward,angle,3)
main()
