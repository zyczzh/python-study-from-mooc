def loadData(filePath):
    fr=open(filePath,'r+')#读写一个文本文件
    lines=fir.readlines()#一次读取整个文件
    reData=[]#存储城市各项消费信息
    retCityName=[]#存储城市名称
    for line in lines:
        items=line.strip().split(",")
        retCityName.append(items[0])
        retData.append([float(items[i])
    for i in range(1,len(items))])
        return retData,retCityName
    
