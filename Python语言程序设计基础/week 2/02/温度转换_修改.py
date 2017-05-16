#TempConvert.py
val=input("请输入带温度表示符号的温度值（例如:32C):")
if val[-1]in['C','c']:
#val[-1]是最后一个字胡串"C"
    f=1.8*eval(val[0:-1])+32
    #val[0:-1]理解为从左0字符开始到右的集合与从右到左不包含左的集合的交际。
    print("转换后的温度为：%.2fF"%f)
elif val[-1]in['F','f']:
    c=(eval(val[0:-1])-32)/1.8
    print("转换后的温度为：%.2fc"%c)
else:
    print("输入有误")
    
   
