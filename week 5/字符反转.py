def reverse(a):
    if a== "":
        return a
    else:
        return reverse(a[1:])+a[0]
#"a"只是一个中间变量，不会影响结果，中间可以是任何字符
