d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d={}
for i,j in d1.items():
    for x,y in d2.items():
        if i==x:
            d[i]=j+y
        elif i!=x:
            d[i]=j
print(d)
 