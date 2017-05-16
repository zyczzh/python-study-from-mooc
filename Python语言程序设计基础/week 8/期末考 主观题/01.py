diet=input().split(' ,')
for i in range(len(diet)):
    for j in range(len(diet)):
        if not(i==j):
            print(diet[i],diet[j])
            #print('{}{}'.format(diet[i],diet[j]))
