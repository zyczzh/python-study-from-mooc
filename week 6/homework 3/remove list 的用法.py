x = ['a', 'b', 'c', 'b']
y = ['b', 'c']
for i in x:
    if i in y:
        x.remove(i)
print(x)
