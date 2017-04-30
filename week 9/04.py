a=input()
def gettext():
    txt=a.lower()
    for ch in 'P':
        txt=txt.replace(ch, "p")
        return txt

hamleTxt=gettext()
words=hamleTxt.split()
counts={}
for word in words:
    if word in counts:
        counts[word]=counts[word]+1
    else:
        counts[word]=1
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(1):
    word,count=items[i]
    print("{0:1}".format(word))
