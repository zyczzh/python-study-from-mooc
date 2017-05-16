import numpy as np
import PIL.Image as image#加载PIL包，用于加载图片
from sklearn.cluster import KMeans#加载Kmeans算法
#loadData函数 
def loadData(filePath):
    f = open(filePath,'rb')
    data = []
    img = image.open(f)#以列表形式返回图片像素
    m,n = img.size#获得图片的大小
    for i in range(m):
        for j in range(n):
            x,y,z = img.getpixel((i,j))
            data.append([x/256.0,y/256.0,z/256.0])
    f.close()
    return np.mat(data),m,n
 
imgData,row,col = loadData('kmeans/bull.jpg')
label = KMeans(n_clusters=4).fit_predict(imgData)
 
label = label.reshape([row,col])
pic_new = image.new("L", (row, col))
for i in range(row):
    for j in range(col):
        pic_new.putpixel((i,j),256 / (label[i][j]+1))
pic_new.save("result-bull-4.jpg", "JPEG")
