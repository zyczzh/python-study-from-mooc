import math
while True:
    a=input("输入您的身高mm:")
    try:
        x=eval(a)
        if type(x)==int:break
    except:pass
while True:
    b=input("输入您的体重kg:")
    try:
        y=eval(b)
        if type(y)==int:break
    except:pass
a=int(a)
b=int(b)
c=a/100
BIM=b/c*2
def main_nation():
    if BIM>30:
        print("国际版：死肥猪！")
    elif BIM>25:
        print("国际版：偏胖，你还要努力哦~！")
    elif BIM>18.5:
        print("国际版：正常")
    else:
        print("国际版：偏瘦")
main_nation()
def main_china():
    if BIM>38:
        print("中国版:死肥猪！")
    elif BIM>24:
        print("中国版:偏胖，你还要努力哦~！")
    elif BIM>18.5:
        print("中国版:正常")
    else:
        print("中国版:偏瘦")
main_china()
