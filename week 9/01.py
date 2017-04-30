s=input()
ilen=s.split(', ').__len__()
x=0
for j in s.split(', '):
    x = x + 1
    if x<ilen:
        s=s+","+j
s_list=s.split(',')
for i in range(0, ilen):
    for j in range(i+1,i+ilen):
        print(s_list[i]+s_list[j])
