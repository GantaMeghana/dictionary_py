dic={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
d={}
for i in dic:
    b=[]
    for j in dic[i]:
        d.update({i:j})
        b.append(d)
print(b)