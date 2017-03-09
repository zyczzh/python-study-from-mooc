import random
colors=[0,0,0,0,0]
for i in range(5):
        g=random.randint(0000,9999)
        while g in colors:
            g=random.randint(0000,9999)
        colors[i]=g
print (colors)
