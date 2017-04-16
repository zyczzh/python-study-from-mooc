import turtle
##全局变量##
#词频排列显示个数
cout=10
#单词频率组数-作为y轴数据
data=[]
#y轴显示凡达倍数-可以根据词频数量进行调节
yScale=6
#x轴显示放大倍数-可以根据count数量进行调节
xScale=30

#######Turtle Start######
#######Turtle End######
#对文本的每一个计算词频的函数
def processLine(line,worldCounts):
    #用空格替换标点符号
    line=replacePunctuations(line)
    #从每一行获取每个词
    words=line.split()
    for word in words:
        if word in wordCounts:
            wordCouts[word]+=1
        else:
            worCounts[word]=1
#空格替换标点函数
def replacePunctuations(line):
    for ch in line:
        if ch in "~@#$%^&*()_-+=<>?/,.:{}[]\'""":
            line=line.replace(ch," ")
        return line
def main():
    #用户输入一个文件名
    filename=input("enter a filename:").strip()
    infile=open(filename,"r")
    #建立用于技术的空字典
    wordCounts={}
    for line in infile:
        processLine(line.lower(),wordCounts)
    #从字典中获取数据对
    pairs=list(wordCounts.items())
    #列表中的数据对交换位置，数据对排序
    items=[[x,y]for(y,x)in pairs]
    items,sort()
    #输出count个数词频结果
    for i in range(len(items)-1,len(item)-count-1,-1):
        print(intems[i][1]+"\t"+str(items[i][0]))
        data.append(items[i][0])
        words.append(items[i][1])
    infile.close()
#调用main（）函数
if __name___=='__main__':
    main()
