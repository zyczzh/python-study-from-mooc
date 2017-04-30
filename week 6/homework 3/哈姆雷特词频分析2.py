#CalHamlet.py
def getText():
    txt=open("hamlet.txt","r").read()
    txt=txt.lower()
    for ch in '!"#$%&()*+,-./;:<=>?@[\\]^_`{|}~':
        txt=txt.replace(ch, " ")#将文本中特殊字符替换为空格
    return txt

hamleTxt=getText()
words=hamleTxt.split()
################
excludes=['the','and','to','of','a','i']#定义需要移除的单词
for i in words:
#循环滤变单词中不需要的单词
    if i in excludes:
        words.remove(i)
################
counts={}
for word in words:
#统计单词出现的次数
    if word in counts:
        counts[word]=counts[word]+1
    else:
        counts[word]=1
#或者使用代码 counts[word]=counts.get(word,0)+1
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count=items[i]
    print("{0:10}{1:>5}".format(word,count))
