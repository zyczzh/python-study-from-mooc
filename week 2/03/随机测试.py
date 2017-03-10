import random
setcolor=['A','B','C','D','E','F',1,2,3,4,5,6,7,8,9,0]
color=random.sample(setcolor,5)#选者六个字符组合
a="#"
for j in color:
    a=a+str(j)#拼接字符
print (a)

#可以看出random是有放回的
for i in range(10):
   print(int(random.random()*10))
