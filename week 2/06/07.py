from turtle import*
fillcolor("red")
begin_fill()
while True:
    forward(200)
    right(144)
    if abs(pos())<1:
        break
end_fill()
# 注意colour和color的区别
