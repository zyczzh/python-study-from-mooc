fo=open("hangwenjian.txt","r")
for line in fo:
    #处理一个数据
    line=fo.readline()#跳过第一行
    print(line[:-4])
fo.close()
