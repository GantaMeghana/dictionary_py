dict1 = {'c1': 'Red', 'c2': 'Green', 'c3':None}
d={}
for i in dict1:
    if dict1[i]!=None:
        d.update({i:dict1[i]})
print(d)

# dict1 = {key:value for (key, value) in dict1.items() if value is not None}
# print(dict1)


