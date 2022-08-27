a=['S001', 'S002', 'S003', 'S004']
b=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
c=[85, 98, 89, 92]
d={}
for i in range(len(a)):
    for i in range(len(b)):
        for i in range(len(c)):
            d.update({a[i]:{b[i]:c[i]}})
print(d)
